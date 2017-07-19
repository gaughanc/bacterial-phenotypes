from django.core.management.base import BaseCommand, CommandError
from wb0.models import Genus, Species

# for each genus, print a list of its attributes

class Command(BaseCommand):
    help = "Exports taxa"

    def handle(self, *args, **options):
    	for Taxon in [Genus, Species]:
    	    for taxon in Taxon.objects.all():
    	        l = []
    	        for field in Taxon._meta.get_fields()[1:]:
    	    	    l.append(field.name + ": " + getattr(taxon, field.name))	
    	        print(l)
