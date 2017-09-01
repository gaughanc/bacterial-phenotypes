from django.core.management.base import BaseCommand, CommandError
from wb0.models import Genus, Species

class Command(BaseCommand):
    help = "Prints functions for retreiving lists of field choices and taxon attributes"

    def handle(self, *args, **options):
        working_genera = ['Bacteroides', 'Prevotella', 'Akkermansia', 'Anaerostripes', 'Anaerotruncas', 'Barnesiella', 'Blautia', 'Roseburia', 'Alloprevotella', 'Porphyromonas', 'Paraprevotella', 'Parabacteroides', 'Oscillibacter', 'Odoribacter', 'Faecalibacterium', 'Enterobacter', 'Shuttleworthia', 'Sediminibacterium', 'Peptoniphilus', 'Moryella', 'Holdemania', 'Gordonibacter', 'Dorea', 'Sutterella', 'Sporobacter', 'Pseudoflavonifractor', 'Flavonifractor', 'Achromobacter', 'Aerococcus', 'Catenibacterium', 'Collinsella', 'Aggregatibacter', 'Anaerococcus', 'Succinivibrio', 'Lachnospira', 'Parasutterella', 'Paralactobacillus', 'Oribacterium', 'Ochrobactrum', 'Murdochiella', 'Mogibacterium', 'Megasphaera', 'Hallella', 'Johnsonella', 'Granulicatella', 'Gemmiger', 'Gardnerella', 'Facklamia', 'Enterococcus', 'Dialister', 'Delftia', 'Cronobacter', 'Citrobacter', 'Chryseobacterium', 'Centipeda', 'Butyricicoccus', 'Bulleidia', 'Brevundimonas', 'Anaeroglobus', 'Arthrobacter', 'Atopobium', 'Bacillus', 'Butyricimonas', 'Deinococcus', 'Helicobacter', 'Microbacterium', 'Pseudobutyrivibrio', 'Schwartzia', 'Succiniclasticum', 'Tannerella', 'Alistipes', 'Catonella', 'Kingella', 'Eremococcus', 'Variovorax', 'Slackia', 'Pyramidobacter', 'Abiotrophia', 'Bordetella', 'Parascardovia', 'Olsenella', 'Jonquetella', 'Xylanibacter', 'Eikenella', 'Christensenella', 'Acidaminococcus', 'Oribaculum', 'Oribaculum', 'Cellulosimicrobium', 'Enterorhabdus', 'Anarosalibacter', 'Murimonas', 'Terrisporobacter', 'Intestinimonas', 'Stenotrophomonas', 'Aminobacter', 'Bradyrhizobium', 'Curvibacter', 'Curvibacter', 'Herbaspirillum', 'Turicibacter', 'Rothia', 'Pedobacter', 'Parvibacter', 'Acidovorax', 'Aeromicrobium', 'Afipia', 'Aquabacterium', 'Aurantimonas', 'Azoarcus', 'Xanthomonas', 'Papillibacter', 'Lachnobacterium', 'Azospira', 'Beutenbergia', 'Micrococcus', 'Polaromonas', 'Pseudoxanthomonas', 'Psychrobacter', 'Sphingobium', 'Sphingomonas', 'Sphingopyxis', 'Sulfuritalea', 'Tsukamurella', 'Undibacterium', 'Bosea', 'Brevibacillus', 'Caulobacter', 'Comamonas', 'Craurococcus', 'Cupriavidus', 'Devosia', 'Dietzia', 'Duganella', 'Dyadobacter', 'Enhydrobacter', 'Hoeflea', 'Hydrotalea', 'Janthinobacterium', 'Bifidobacterium', 'Kocuria', 'Limnobacter', 'Mesorhizobium', 'Methylophilus', 'Methyloversatilis', 'Microlunatus', 'Niastella', 'Novosphingobium', 'Olivibacter', 'Paracoccus', 'Patulibacter', 'Wautersiella', 'Actinobaculum', 'Anaerotruncus']
        working_species = [['Bacteroides vulgatus', 'Bacteroides acidifaciens', 'Bacteroides caecimuris', 'Bacteroides ovatus', 'Bacteroides xylanisolvens', 'Bacteroides amylophilus', 'Bacteroides barnesiae', 'Bacteroides bivius', 'Bacteroides buccae', 'Bacteroides caccae', 'Bacteroides caecicola', 'Bacteroides caecigallinarum', 'Bacteroides cellulosilyticus', 'Bacteroides cellulosolvens', 'Bacteroides chinchillae', 'Bacteroides clarus', 'Bacteroides coagulans', 'Bacteroides coprocola', 'Bacteroides coprophilus', 'Bacteroides coprosuis', 'Bacteroides corporis', 'Bacteroides disiens', 'Bacteroides distasonis', 'Bacteroides dorei', 'Bacteroides eggerthii', 'Bacteroides faecichinchillae', 'Bacteroides faecis', 'Bacteroides finegoldii', 'Bacteroides fluxus', 'Bacteroides forsythus', 'Bacteroides gallinaceum', 'Bacteroides gallinarum', 'Bacteroides gingivalis', 'Bacteroides gracilis', 'Bacteroides graminisolvens', 'Bacteroides heparinolyticus', 'Bacteroides intermedius', 'Bacteroides intestinalis', 'Bacteroides levii', 'Bacteroides loescheii', 'Bacteroides luti', 'Bacteroides massiliensis', 'Bacteroides microfusus', 'Bacteroides multiacidus', 'Bacteroides oleiciplenus', 'Bacteroides oralis', 'Bacteroides oris', 'Bacteroides oulorum'], ['Prevotella amnii', 'Prevotella copri'], ['Akkermansia muciniphila'], ['Anaerostripes butyraticus'], [], ['Barnesiella viscericola'], ['Blautia faecis', 'Blautia wexlerae', 'Blautia caecimuris', 'Blautia coccoides', 'Blautia stercoris', 'Blautia wexlerae'], ['Roseburia cecicola', 'Roseburia faecis', 'Roseburia hominis', 'Roseburia inulinivorans'], ['Alloprevotella tannerae', 'Alloprevotella rava'], ['Porphyromonas asaccharolytica', 'Porphyromonas gingivalis'], ['Paraprevotella clara'], ['Parabacteroides distasonis', 'Parabacteroides goldsteinii', 'Parabacteroides merdae', 'Parabacteroides johnsonii'], ['Oscillibacter valericigenes', 'Oscillibacter ruminantium'], ['Odoribacter denticanis'], ['Faecalibacterium prausnitzii'], [], ['Shuttleworthia satelles'], ['Sediminibacterium salmoneum'], ['Peptoniphilus asaccharolyticus'], ['Moryella indoligenes'], ['Holdemania filiformis'], ['Gordonibacter pamelaeae'], ['Dorea formicigenerans', 'Dorea longicatena'], ['Sutterella wadsworthensis'], ['Sporobacter termitidis'], ['Pseudoflavonifractor capillosus'], ['Flavonifractor plautii'], ['Achromobacter xylosoxidans'], ['Aerococcus christensenii'], ['Catenibacterium mitsuokai'], ['Collinsella aerofaciens'], ['Aggregatibacter actinomycetemcomitans'], ['Anaerococcus prevotii', 'Anaerococcus tetradius', 'Anaerococcus hydrogenalis', 'Anaerococcus lactolyticus', 'Anaerococcus octavius', 'Anaerococcus vaginalis'], ['Succinivibrio dextrinosolvens'], ['Lachnospira multipara'], ['Parasutterella excrementihominis'], ['Paralactobacillus selangorensis'], ['Oribacterium sinus'], ['Ochrobactrum anthropi'], ['Murdochiella asaccharolytica'], ['Mogibacterium pumilum', 'Mogibacterium vescum'], ['Megasphaera micronuciformis'], ['Hallella seregens'], ['Johnsonella ignava'], ['Granulicatella adiacens', 'Granulicatella elegans', 'Granulicatella balaenopterae'], [], ['Gardnerella vaginalis'], ['Facklamia hominis'], ['Enterococcus faecalis', 'Enterococcus faecium', 'Enterococcus gallinarum', 'Enterococcus hirae'], ['Dialister pneumosintes'], ['Delftia acidovorans'], [], [], [], ['Centipeda periodontii'], ['Butyricicoccus pullicaecorum'], ['Bulleidia extructa'], ['Brevundimonas diminuta', 'Brevundimonas vesicularis'], ['Anaeroglobus geminatus'], ['Arthrobacter agilis'], ['Atopobium deltae'], ['Bacillus thermoamylovorans'], ['Butyricimonas synergistica', 'Butyricimonas virosa'], [], ['Helicobacter pylori', 'Helicobacter mustelae'], ['Microbacterium immunditiarum'], ['Pseudobutyrivibrio ruminis'], ['Schwartzia succinivorans'], ['Succiniclasticum ruminis'], ['Tannerella forsythia'], ['Alistipes indistinctus', 'Alistipes inops', 'Alistipes onderdonkii', 'Alistipes shahii'], ['Catonella morbi'], ['Kingella orale'], ['Eremococcus coleocola'], ['Variovorax paradoxus'], [], ['Pyramidobacter piscolens'], [], ['Bordetella petrii'], [], ['Olsenella uli'], ['Jonquetella antrhopi'], ['Xylanibacter oryzae'], ['Eikenella corrodens'], ['Christensenella minuta'], ['Acidaminococcus fermentans'], ['Oribaculum catoniae'], ['Oribaculum catoniae'], ['Cellulosimicrobium cellulans'], ['Enterorhabdus mucosicola', 'Enterorhabdus caecimuris'], [], ['Murimonas intestini'], [], ['Intestinimonas butyriciproducens'], ['Stenotrophomonas maltophilia'], ['Aminobacter aminovorans', 'Aminobacter aganoensis'], ['Bradyrhizobium japonicum'], ['Curvibacter gracilis', 'Curvibacter gracilis'], ['Curvibacter gracilis', 'Curvibacter gracilis'], ['Herbaspirillum seropedicae'], ['Turicibacter sanguinis'], ['Rothia aeria', 'Rothia nasimurium'], ['Pedobacter heparinus'], ['Parvibacter caecicola'], ['Acidovorax  facilis'], ['Aeromicrobium'], ['Afipia felis'], ['Aquabacterium commune'], ['Aurantimonas coralicida'], ['Azoarcus indigens'], [], ['Papillibacter cinnamivorans'], ['Lachnobacterium bovis'], ['Azospira oryzae'], ['Beutenbergia cavernae'], [], ['Polaromonas vacuolata'], [], ['Psychrobacter immobilis'], ['Sphingobium yanoikuyae'], [], ['Sphingopyxis macrogoltabida'], ['Sulfuritalea hydrogenivorans'], ['Tsukamurella paurometabolum'], ['Undibacterium pigrum'], ['Bosea thiooxidans'], [], [], ['Comamonas terrigena'], ['Craurococcus roseus'], [], ['Devosia riboflavina'], ['Dietzia maris'], ['Duganella zoogloeoides'], ['Dyadobacter fermentans'], ['Enhydrobacter aerosaccus'], ['Hoeflea marina'], ['Hydrotalea flava'], [], ['Bifidobacterium dentium', 'Bifidobacterium animalis'], ['Kocuria rosea'], ['Limnobacter thiooxidans'], [], ['Methylophilus methylotrophus'], ['Methyloversatilis universalis'], ['Microlunatus phosphovorus'], ['Niastella koreensis'], [], ['Olivibacter sitiensis'], [], ['Patulibacter minatonensis'], ['Wautersiella falsenii'], ['Actinobaculum suis'], ['Anaerotruncus colihominis', 'Anaerotruncus colihominis']]
        # define lists
        addedgenera = []
        genera, catcount, g_oxygen, g_morph, g_motil, g_spore, g_gram, g_bile, g_sacc, ox_choices, morph_choices = [], [], [], [], [], [], [], [], [], [], [] 
        lists = [genera, catcount, g_oxygen, g_morph, g_motil, g_spore, g_gram, g_bile, g_sacc, ox_choices, morph_choices]
        lnames = ["genera", "catcount", "g_oxygen", "g_morph", "g_motil", "g_spore", "g_gram", "g_bile", "g_sacc", "ox_choices", "morph_choices"]
        #define field names, starting at aerobic_status
        fields = []
        for f in Species._meta.get_fields()[3:]:
            fields.append(f.name)
        # build field choices lists
        for i, l in enumerate(lists[9:]):
            for choice in Species._meta.get_field(fields[i]).choices:
                l.append(choice[0])
        # build all genera-length lists
        for i, g in enumerate(Genus.objects.all()):
            genusname = getattr(g, "name")
            genera.append(genusname)
            catcount.append([0, 0])
            for i, l in enumerate(lists[2:9]):
                l.append(getattr(g, fields[i]))
            # Fudge, include deleted repeats to match working version
            if genusname == "Oribaculum" or genusname == "Curvibacter":
                genera.append(genusname)
                catcount.append([0, 0])
                for i, l in enumerate(lists[2:9]):
                    l.append(getattr(g, fields[i])) 
            if genera == working_genera:
                break
        # manually add Strep and Staph
        for i, g in enumerate(Genus.objects.all()):
            genusname = getattr(g, "name")
            if genusname == "Streptococcus" or genusname == "Staphylococcus":
                addedgenera.append(genusname)
                genera.append(genusname)
                catcount.append([0, 0])
                for i, l in enumerate(lists[2:9]):
                    l.append(getattr(g, fields[i]))
        # write python functions
        for i, lname in enumerate(lnames):
            print("\n".join(["def get_{}():".format(lname), "    {} = {}".format(lname, lists[i]), "    return {}".format(lname), ""]))


        species, s_oxygen, s_morph, s_motil, s_spore, s_gram, s_bile, s_sacc, cat, urease = [], [], [], [], [], [], [], [], [], [] 
        lists = [species, s_oxygen, s_morph, s_motil, s_spore, s_gram, s_bile, s_sacc, cat, urease]
        lnames = ["species", "s_oxygen", "s_morph", "s_motil", "s_spore", "s_gram", "s_bile", "s_sacc", "cat", "urease"]
        fields = ["aerobic_status", "morphology", "motility", "spore_formation", "gram_stain", "bile_sensitive", "saccharolytic", "catalase", "urease"]
        for i, genus in enumerate(working_genera):
            for l in lists:
                l.append([])
            for s in Species.objects.all():
                speciesname = getattr(s, "name")
                if genus in speciesname:
                    species[i].append(speciesname)
                    for j, l in enumerate(lists[1:]):
                        l[i].append(getattr(s, fields[j]))
                if species[i] == working_species[i]:
                    break
        # manually add Strep and Staph
        for i, addedgenus in enumerate(addedgenera):
            for l in lists:
                l.append([])
            for s in Species.objects.all():
                speciesname = getattr(s, "name")
                if addedgenus in speciesname:
                    species[-1].append(speciesname)
                    for j, l in enumerate(lists[1:]):
                        l[-1].append(getattr(s, fields[j]))
        for i, lname in enumerate(lnames):
            print("\n".join(["def get_{}():".format(lname), "    {} = {}".format(lname, lists[i]), "    return {}".format(lname), ""]))        
