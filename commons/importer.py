from collections import namedtuple

import pandas as pd
from django.core.management import BaseCommand, CommandError
from django.db import IntegrityError


class ImportTSVFileCommand(BaseCommand):
    help = 'Imports .tsv files to database tables'
    chunk_size = 10 ** 5
    model_class = None
    _record_cls = None

    def add_arguments(self, parser):
        parser.add_argument(
            '--file_path',
            action='store',
            dest='file_path',
            help='Path to file, which will be imported',
        )
        parser.add_argument(
            '--chunk_size',
            action='store',
            dest='chunk_size',
            help='Chunk size',
        )

    def handle(self, *args, **options):
        file_path = options['file_path']

        if not file_path:
            raise CommandError(f'Please give --file_path=... argument')

        chunk_size = options.get('chunk_size', self.chunk_size) or self.chunk_size

        self.pre_process()

        try:
            data = pd.read_csv(file_path, chunksize=chunk_size, iterator=True, delimiter='\t')
        except pd.parser.CParserError as exc:
            raise CommandError(f'Error tokenizing data: {exc}')
        except (FileNotFoundError, IOError) as exc:
            raise CommandError(f'Error reading file {file_path}: {exc}')

        self.stdout.write(self.style.SUCCESS(f'Processing file {file_path}'))

        count = 0

        for chunk in data:
            result, m2m_result = self.process(chunk)
            if result:
                try:
                    self.model_class.objects.bulk_create(result, batch_size=10 ** 4)
                except IntegrityError as exc:
                    self.stderr.write(self.style.ERROR(f'Cannot insert records to DB table: {exc}'))
                else:
                    self.process_m2m(m2m_result)
                    count += len(result)
                    self.stdout.write(f'{count} records already stored in database')

        self.stdout.write(self.style.SUCCESS(f'Operation finished successful'))

    def pre_process(self, chunk):
        raise NotImplementedError('should be implemented in subclass')

    def process(self, chunk):
        raise NotImplementedError('should be implemented in subclass')

    def process_m2m(self, data):
        raise NotImplementedError('should be implemented in subclass')

    def _get_record_cls(self, data):
        if self._record_cls is None:
            self._record_cls = namedtuple('Record', list(data.columns))
        return self._record_cls
