from django.core.management.base import BaseCommand, CommandError
from wb0.models import Genus

# for each genus, print its list of attributes

class Command(BaseCommand):
    help = "Exports genera"

    def handle(self, *args, **options):
        fields = Genus._meta.get_fields()[1:]
        l = []
        for field in fields:
            l.append(field.name)
        print("\t".join(l))
        for genus in Genus.objects.all():
            l = []
            for field in fields:
                l.append(getattr(genus, field.name))	
            print("\t".join(l))
