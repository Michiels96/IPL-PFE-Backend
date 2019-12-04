from django.contrib import admin
from .models import Enfants, Handicap, HandicapEnfant

admin.site.register(Enfants)
admin.site.register(Handicap)
admin.site.register(HandicapEnfant)