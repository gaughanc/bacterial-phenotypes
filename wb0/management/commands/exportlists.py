from django.core.management.base import BaseCommand, CommandError
from wb0.models import Genus, Species

class Command(BaseCommand):
    help = "Prints list of genera names and grouped list of species names"

    def handle(self, *args, **options):
        genera = []
        species = []
        catalase = []
        catcount = []
        for i, g in enumerate(Genus.objects.all()):
            genusname = getattr(g, "name")
            genera.append(genusname)
            for l in [species, catalase]:
                l.append([])
            catcount.append([0, 0])
            if genusname == "Anearotruncas":
                break
            for s in Species.objects.all():
                speciesname = getattr(s, "name")
                if genusname in speciesname:    
                    species[i].append(speciesname)
                    catalase[i].append(getattr(s, "catalase"))
                if speciesname == "Bacteroides oulorum":
                    break 
        print(genera)
        #print(species)
        #print(catalase)
        #print(catcount)
