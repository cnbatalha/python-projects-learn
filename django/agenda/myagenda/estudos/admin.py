from django.contrib import admin

from .models import Materia
from .models import Topico

class TopicoInline(admin.TabularInline):
    model = Topico
    extra = 1
    
class MateriaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nome']}),
        ('Date information', {'fields': ['data_criacao'], 'classes': ['collapse']}),
    ]
    inlines = [TopicoInline]    

admin.site.register(Materia, MateriaAdmin)