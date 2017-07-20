from django.core.management.base import BaseCommand, CommandError
from wb0.models import Genus

class Command(BaseCommand):
    help = "Prints attributes of each genus"

    def handle(self, *args, **options):
        fields = Genus._meta.get_fields()[1:]
        print("\t".join(field.name for field in fields))
        for genus in Genus.objects.all():	
            print("\t".join(getattr(genus, field.name) for field in fields))
