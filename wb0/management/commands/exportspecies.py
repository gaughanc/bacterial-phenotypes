from django.core.management.base import BaseCommand, CommandError
from wb0.models import Species

class Command(BaseCommand):
    help = "Prints attributes of each species"

    def handle(self, *args, **options):
        fields = Species._meta.get_fields()[1:]
        print("\t".join(field.name for field in fields))
        for species in Species.objects.all():	
            print("\t".join(getattr(species, field.name) for field in fields))
