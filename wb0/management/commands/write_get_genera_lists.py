from django.core.management.base import BaseCommand, CommandError
from wb0.models import Genus, Species

class Command(BaseCommand):
    help = "Prints functions for retreiving lists of genera and genera attributes"

    def handle(self, *args, **options):
        working_genera = ['Bacteroides', 'Prevotella', 'Akkermansia', 'Anaerostripes', 'Anaerotruncas', 'Barnesiella', 'Blautia', 'Roseburia', 'Alloprevotella', 'Porphyromonas', 'Paraprevotella', 'Parabacteroides', 'Oscillibacter', 'Odoribacter', 'Faecalibacterium', 'Enterobacter', 'Shuttleworthia', 'Sediminibacterium', 'Peptoniphilus', 'Moryella', 'Holdemania', 'Gordonibacter', 'Dorea', 'Sutterella', 'Sporobacter', 'Pseudoflavonifractor', 'Flavonifractor', 'Achromobacter', 'Aerococcus', 'Catenibacterium', 'Collinsella', 'Aggregatibacter', 'Anaerococcus', 'Succinivibrio', 'Lachnospira', 'Parasutterella', 'Paralactobacillus', 'Oribacterium', 'Ochrobactrum', 'Murdochiella', 'Mogibacterium', 'Megasphaera', 'Hallella', 'Johnsonella', 'Granulicatella', 'Gemmiger', 'Gardnerella', 'Facklamia', 'Enterococcus', 'Dialister', 'Delftia', 'Cronobacter', 'Citrobacter', 'Chryseobacterium', 'Centipeda', 'Butyricicoccus', 'Bulleidia', 'Brevundimonas', 'Anaeroglobus', 'Arthrobacter', 'Atopobium', 'Bacillus', 'Butyricimonas', 'Deinococcus', 'Helicobacter', 'Microbacterium', 'Pseudobutyrivibrio', 'Schwartzia', 'Succiniclasticum', 'Tannerella', 'Alistipes', 'Catonella', 'Kingella', 'Eremococcus', 'Variovorax', 'Slackia', 'Pyramidobacter', 'Abiotrophia', 'Bordetella', 'Parascardovia', 'Olsenella', 'Jonquetella', 'Xylanibacter', 'Eikenella', 'Christensenella', 'Acidaminococcus', 'Oribaculum', 'Oribaculum', 'Cellulosimicrobium', 'Enterorhabdus', 'Anarosalibacter', 'Murimonas', 'Terrisporobacter', 'Intestinimonas', 'Stenotrophomonas', 'Aminobacter', 'Bradyrhizobium', 'Curvibacter', 'Curvibacter', 'Herbaspirillum', 'Turicibacter', 'Rothia', 'Pedobacter', 'Parvibacter', 'Acidovorax', 'Aeromicrobium', 'Afipia', 'Aquabacterium', 'Aurantimonas', 'Azoarcus', 'Xanthomonas', 'Papillibacter', 'Lachnobacterium', 'Azospira', 'Beutenbergia', 'Micrococcus', 'Polaromonas', 'Pseudoxanthomonas', 'Psychrobacter', 'Sphingobium', 'Sphingomonas', 'Sphingopyxis', 'Sulfuritalea', 'Tsukamurella', 'Undibacterium', 'Bosea', 'Brevibacillus', 'Caulobacter', 'Comamonas', 'Craurococcus', 'Cupriavidus', 'Devosia', 'Dietzia', 'Duganella', 'Dyadobacter', 'Enhydrobacter', 'Hoeflea', 'Hydrotalea', 'Janthinobacterium', 'Bifidobacterium', 'Kocuria', 'Limnobacter', 'Mesorhizobium', 'Methylophilus', 'Methyloversatilis', 'Microlunatus', 'Niastella', 'Novosphingobium', 'Olivibacter', 'Paracoccus', 'Patulibacter', 'Wautersiella', 'Actinobaculum', 'Anaerotruncus']
        genera, catcount, g_oxygen, g_morph, g_motil, g_spore, g_gram, g_bile, g_sacc = [], [], [], [], [], [], [], [], [] 
        lists = [genera, catcount, g_oxygen, g_morph, g_motil, g_spore, g_gram, g_bile, g_sacc]
        lnames = ["genera", "catcount", "g_oxygen", "g_morph", "g_motil", "g_spore", "g_gram", "g_bile", "g_sacc"]
        attribs = ["aerobic_status", "morphology", "motility", "spore_formation", "gram_stain", "bile_sensitive", "saccharolytic"]
        for i, g in enumerate(Genus.objects.all()):
            genusname = getattr(g, "name")
            genera.append(genusname)
            catcount.append([0, 0])
            for i, l in enumerate(lists[2:]):
                l.append(getattr(g, attribs[i]))
            # Fudge, include deleted repeats to match working version
            if genusname == "Oribaculum" or genusname == "Curvibacter":
                genera.append(genusname)
                catcount.append([0, 0])
                for i, l in enumerate(lists[2:]):
                    l.append(getattr(g, attribs[i])) 
            if genera == working_genera:
                break
        # write python functions
        for i, lname in enumerate(lnames):
            print("\n".join(["def get_{}():".format(lname), "    {} = {}".format(lname, lists[i]), "    return {}".format(lname), ""]))

