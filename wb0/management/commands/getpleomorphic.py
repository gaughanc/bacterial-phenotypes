from django.core.management.base import BaseCommand, CommandError
from wb0.models import Genus, Species

class Command(BaseCommand):
    help = "Prints pleomorphic entries made before pleomorphic rods was an option"

    def handle(self, *args, **options):
        for taxon in (Genus, Species):
            pleo = []
            for t in taxon.objects.all():
                morph = getattr(t, "morphology")
                if morph == "pleomorphic":
                    pleo.append(getattr(t, "name"))
                elif morph == "pleomorphic rods":
                    break
            print(str(pleo))
 

