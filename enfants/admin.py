from django.contrib import admin
from .models import Enfants, Handicaps, HandicapEnfant

admin.site.register(Enfants)
admin.site.register(Handicaps)
admin.site.register(HandicapEnfant)