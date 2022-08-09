from django.contrib import admin
from .models import Quarry, Hour, Line, Silo, Action, Quarter

admin.site.register(Quarry)
admin.site.register(Hour)
admin.site.register(Quarter)
admin.site.register(Line)
admin.site.register(Silo)
admin.site.register(Action)


