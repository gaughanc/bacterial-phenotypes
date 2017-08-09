from django.db import models


def make_choices(*xs):
    xs = list(xs)
    xs.append("not indicated")
    return [(x, x) for x in xs]


class Taxon(models.Model):
    name = models.CharField(max_length=100)
    doi = models.CharField(max_length=100)

    AEROBE_CHOICES = make_choices(
        "aerobe", "facultative anaerobe", "microaerobe", "obligate anaerobe",
    	"anaerobe (unspecified)", "microaerobe or anaerobe", "microaerobe or aerobe",
        "aerotolerant")
    aerobic_status = models.CharField(max_length=100, choices=AEROBE_CHOICES)

    MORPHOLOGY_CHOICES = make_choices(
        "rod/ bacilli", "slightly curved rods", "cocci", "oval-shaped/ coccobaccili",
        "fusiform", "rods or oval-shaped", "cocci or oval-shaped",
        "rods or slightly curved rods", "ovoid", "pleomorphic", "rods, cocci, or oval-shaped",
        "rods or cocci", "pleomorphic rods", "pleomorphic cocci")
    morphology = models.CharField(max_length=100, choices=MORPHOLOGY_CHOICES)

    MOTILITY_CHOICES = make_choices("motile", "non-motile", "variable")
    motility = models.CharField(max_length=100, choices=MOTILITY_CHOICES)

    SPORE_CHOICES = make_choices("spore forming", "non-spore forming", "mixed")   
    spore_formation = models.CharField(max_length=100, choices=SPORE_CHOICES)

    GRAM_CHOICES = make_choices(
        "Gram-positive", "Gram-negative", "Gram-variable")
    gram_stain = models.CharField(max_length=100, choices=GRAM_CHOICES)

    BILE_CHOICES = make_choices(
        "growth in 20% bile", "no growth in 20% bile", "somewhat inhibited by 20% bile",
        "mixed")
    bile_sensitive = models.CharField(max_length=100, choices=BILE_CHOICES)

    SACCHAROLYTIC_CHOICES = make_choices(
    	"saccharolytic", "asaccharolytic", "mixed")
    saccharolytic = models.CharField(
        max_length=100, choices=SACCHAROLYTIC_CHOICES)

    comments = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return "{0} - http://dx.doi.org/{1}".format(self.name, self.doi)

    class Meta:
        abstract = True


class Genus(Taxon):
    class Meta:
        verbose_name_plural = "genera"


class Species(Taxon):
    UREASE_CHOICES = make_choices(
        "urease positive", "urease negative", "urease variable")
    urease = models.CharField(max_length=20, choices=UREASE_CHOICES)

    CATALASE_CHOICES = make_choices(
        "catalase positive", "catalase negative", "catalase variable")
    catalase = models.CharField(max_length=20, choices=CATALASE_CHOICES)
    
    FATTYACID_CHOICES = make_choices(
        "consumed", "major product", "minor product", "not producted")
    formate_production = models.CharField(max_length=100, choices=FATTYACID_CHOICES)
    acetate_production = models.CharField(max_length=100, choices=FATTYACID_CHOICES)
    propionate_production = models.CharField(max_length=100, choices=FATTYACID_CHOICES)
    butyrate_production = models.CharField(max_length=100, choices=FATTYACID_CHOICES)
    isobutyrate_production = models.CharField(max_length=100, choices=FATTYACID_CHOICES)
    valerate_production = models.CharField(max_length=100, choices=FATTYACID_CHOICES)
    isovalerate_production = models.CharField(max_length=100, choices=FATTYACID_CHOICES)  

    class Meta:
        verbose_name_plural = "species"
