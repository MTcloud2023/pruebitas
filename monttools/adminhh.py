from django.contrib import admin
from .models import PrimeraTabla, SegundaTabla
# Register your models here.
class SegundaTablaInline(admin.TabularInline):
    model = SegundaTabla
    extra = 1

@admin.register(PrimeraTabla)
class PrimeraTablaAdmin(admin.ModelAdmin):
    inlines = [SegundaTablaInline]

@admin.register(SegundaTabla)
class SegundaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio', 'montador']
    search_fields = ['folio__folio', 'montador'] 