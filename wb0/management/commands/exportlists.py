from django.core.management.base import BaseCommand, CommandError
from wb0.models import Genus, Species

class Command(BaseCommand):
    help = "Prints list of genera names and grouped list of species names"

    def handle(self, *args, **options):
        genera = []
        species = []
        catalase = []
        for i, g in enumerate(Genus.objects.all()):
            genusname = getattr(g, "name")
            genera.append(genusname)
            species.append([])
            catalase.append([])
            for s in Species.objects.all():
                speciesname = getattr(s, "name")
                if genusname in speciesname:    
                    species[i].append(speciesname)
                    catalase[i].append(getattr(s, "catalase"))
        #print(genera)
        #print(species)
        #print(catalase)
