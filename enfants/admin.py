from django.contrib import admin
from .models import Enfant, Handicap, HandicapEnfant,InfoSupplementaire,PersonneContact

admin.site.register(Enfant)
admin.site.register(Handicap)
admin.site.register(HandicapEnfant)
admin.site.register(InfoSupplementaire)
admin.site.register(PersonneContact)