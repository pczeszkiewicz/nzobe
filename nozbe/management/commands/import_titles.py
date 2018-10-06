from commons.importer import ImportTSVFileCommand
from commons.utils import obj_or_none
from nozbe.models import Title


class Command(ImportTSVFileCommand):
    help = 'Imports names'
    model_class = Title

    def pre_process(self):
        pass

    def process_m2m(self, data):
        pass

    def process(self, data):
        result = []

        record_cls = self._get_record_cls(data)
        model_class = self.model_class
        for i, record in data.iterrows():
            record = record_cls(*record)
            if not obj_or_none(record.primaryTitle) or record.primaryTitle.find('\t') >= 0:
                self.stdout.write(f'Incorrect content in {record.tconst} - skipped')
                continue

            result.append(model_class(
                id=record.tconst,
                title_type=record.titleType,
                primary_title=record.primaryTitle,
                original_title=record.originalTitle,
                is_adult=record.isAdult,
                start_year=obj_or_none(record.startYear),
                end_year=obj_or_none(record.endYear),
                runtime_minutes=obj_or_none(record.runtimeMinutes),
                genres=record.genres.split(',') if obj_or_none(record.genres) else None
            ))

        return result, {}
