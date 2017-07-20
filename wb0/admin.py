from django.contrib import admin

from .models import Genus

admin.site.register(Genus)

from .models import Species

admin.site.register(Species)
