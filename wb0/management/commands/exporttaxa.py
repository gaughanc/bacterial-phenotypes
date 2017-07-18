from django.core.management.base import BaseCommand, CommandError
from wb0.models import Genus

# for each genus, print a list of its attributes

class Command(BaseCommand):
    help = "Exports taxa"

    def handle(self, *args, **options):
    	for genus in Genus.objects.all():
    	    l = []
    	    for field in Genus._meta.get_fields()[1:]:
    	    	l.append(field.attname)	
    	    print(l)

# TODO: apply to species
