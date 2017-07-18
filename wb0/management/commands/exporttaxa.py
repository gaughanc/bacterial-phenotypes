from django.core.management.base import BaseCommand, CommandError
from wb0.models import Genus

# for each genus, print a list of its attributes

class Command(BaseCommand):
    help = "Exports taxa"

    def handle(self, *args, **options):
    	all_genera = Genus.objects.all()
    	all_fields = Genus._meta.get_fields()
    	for genus in all_genera:
    	    l = []
    	    for field in all_fields[1:]:
    	        l.append(field)	
    	        print(l)

# TODO: apply to species as well
