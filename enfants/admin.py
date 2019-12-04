from django.contrib import admin
from .models import Enfant, Handicap, HandicapEnfant

admin.site.register(Enfant)
admin.site.register(Handicap)
admin.site.register(HandicapEnfant)