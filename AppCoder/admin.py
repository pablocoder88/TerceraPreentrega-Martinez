from django.contrib import admin
from .models import Competencia, Entrenador, Nadador

class CompetenciaAdmin(admin.ModelAdmin):
  list_display = ['nombre', 'camada']
  search_fields = ['nombre', 'camada']
  list_filter = ['nombre']

# Register your models here.
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Entrenador)
admin.site.register(Nadador)


