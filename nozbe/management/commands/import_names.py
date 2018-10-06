from django.core.management import CommandError

from commons.importer import ImportTSVFileCommand
from commons.utils import obj_or_none
from nozbe.models import Name, Title


class Command(ImportTSVFileCommand):
    help = 'Imports names'
    model_class = Name

    def pre_process(self):
        if not Title.objects.exists():
            raise CommandError(
                'Importing names before import title does not make sense. '
                'Please import titles first'
            )

    def process_m2m(self, data):
        for name_id, known_for_titles in data['known_for_titles'].items():
            if known_for_titles:
                obj = self.model_class.objects.get(pk=name_id)
                obj.known_for_titles.add(*known_for_titles)

    def process(self, data):
        result = []
        known_for_titles = {}

        record_cls = self._get_record_cls(data)

        for record in data.values:
            record = record_cls(*record)

            obj = self.model_class(
                id=record.nconst,
                primary_name=record.primaryName,
                birth_year=obj_or_none(record.birthYear),
                death_year=obj_or_none(record.deathYear),
                primary_profession=record.primaryProfession.split(',') if obj_or_none(
                    record.primaryProfession) else None
            )

            result.append(obj)
            known_for_titles[record.nconst] = record.knownForTitles.split(',') if obj_or_none(
                record.knownForTitles) else None

        return result, {'known_for_titles': known_for_titles}
