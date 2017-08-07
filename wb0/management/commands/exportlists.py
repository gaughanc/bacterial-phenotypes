from django.core.management.base import BaseCommand, CommandError
from wb0.models import Genus, Species

class Command(BaseCommand):
    help = "Prints list of genera names and grouped list of species names"

    def handle(self, *args, **options):
        genera = []
        species = []
        i = 0
        for g in Genus.objects.all():
            genusname = getattr(g, "name")
            genera.append(genusname)
            species.append([])
            for s in Species.objects.all():
                speciesname = getattr(s, "name")
                if genusname in speciesname:    
                    species[i].append(speciesname)
            i += 1
        print(genera)
        print(species)
