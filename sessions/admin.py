from django.contrib import admin
from .models import Session, Question, Note

admin.site.register(Session)
admin.site.register(Question)
admin.site.register(Note)