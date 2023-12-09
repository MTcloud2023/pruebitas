from django.contrib import admin
from.models import *

# Register your models here.

# Register your models here.
class Taskadmin(admin.ModelAdmin):
    readonly_fields = ('created',)   
admin.site.register(Task,Taskadmin)


class admincentros(admin.ModelAdmin):
    readonly_fields = () 
admin.site.register(Centros,admincentros)

class adminprod(admin.ModelAdmin):
    readonly_fields = ()   
admin.site.register(Productos,adminprod)



class SegundaTablaInline(admin.TabularInline):
    model = Registro_forja
    extra = 1
class TerceraTablaInline(admin.TabularInline):
    model = Ajuste_forja
    extra = 1
class CuartaTablaInline(admin.TabularInline):
    model = Fin_forja
    extra = 1
class QuintaTablaInline(admin.TabularInline):
    model = Registro_recorte
    extra = 1
class SextaTablaInline(admin.TabularInline):
    model = Ajuste_recorte
    extra = 1
class SeptimaTablaInline(admin.TabularInline):
    model = Fin_recorte
    extra = 1
class OctavaTablaInline(admin.TabularInline):
    model = Registro_laminado
    extra = 1
class NovenaTablaInline(admin.TabularInline):
    model = Ajuste_laminado
    extra = 1
class DecimaTablaInline(admin.TabularInline):
    model = Fin_laminado
    extra = 1
class DecimaprimeraTablaInline(admin.TabularInline):
    model = Registro_PP
    extra = 1
class DecimasegundaTablaInline(admin.TabularInline):
    model = Ajuste_PP
    extra = 1
class DecimaterceraTablaInline(admin.TabularInline):
    model = Fin_PP
    extra = 1
class DecimacuartaTablaInline(admin.TabularInline):
    model = Registro_PD
    extra = 1
class DecimaquintaTablaInline(admin.TabularInline):
    model = Ajuste_PD
    extra = 1
class DecimasextaTablaInline(admin.TabularInline):
    model = Fin_PD
    extra = 1
class DecimaseptimaTablaInline(admin.TabularInline):
    model = Registro_planchado
    extra = 1
class DecimaoctavaTablaInline(admin.TabularInline):
    model = Ajuste_planchado
    extra = 1
class DecimonovenaTablaInline(admin.TabularInline):
    model = Fin_planchado
    extra = 1
class VigecimaTablaInline(admin.TabularInline):
    model = Registro_hs
    extra = 1
class VigecimaprimeraTablaInline(admin.TabularInline):
    model = Ajuste_hs
    extra = 1
class VigecimasegundaTablaInline(admin.TabularInline):
    model = Fin_hs
    extra = 1    

@admin.register(datos_principales)
class PrimeraTablaAdmin(admin.ModelAdmin):
    inlines = [SegundaTablaInline,TerceraTablaInline,CuartaTablaInline,QuintaTablaInline,SextaTablaInline,SeptimaTablaInline,OctavaTablaInline,NovenaTablaInline,DecimaTablaInline,DecimaprimeraTablaInline,DecimasegundaTablaInline,DecimaterceraTablaInline,DecimacuartaTablaInline,DecimaquintaTablaInline,DecimasextaTablaInline,DecimaseptimaTablaInline,DecimaoctavaTablaInline,DecimonovenaTablaInline,VigecimaTablaInline,VigecimaprimeraTablaInline,VigecimasegundaTablaInline]

@admin.register(Registro_forja)
class SegundaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Montador', 'Auxiliar', 'Inicio', 'Fin',
                  'Altura_Dado_Inferior', 'Altura_Dado_Superior', 'Altura_Calza_Inferior', 'Altura_Calza_Superior', 'Altura_Total',
                  'Altura_Botador_Inferior_Previo', 'Altura_Botador_Inferior_Final', 'Altura_Botador_Superior_Previo', 'Altura_Botador_Superior_Final', 'Altura_Calza_Superior_Trasera',
                  'Altura_Calza_Superior_Izquierda', 'Altura_Calza_Superior_Derecha', 'Altura_Calza_Inferior_Trasera', 'Altura_Calza_Inferior_Izquierda', 'Altura_Calza_Inferior_Derecha',
                  'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
                  'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones']
    search_fields = ['folio__folio','Montador', 'Auxiliar', 'Inicio', 'Fin',
                  'Altura_Dado_Inferior', 'Altura_Dado_Superior', 'Altura_Calza_Inferior', 'Altura_Calza_Superior', 'Altura_Total',
                  'Altura_Botador_Inferior_Previo', 'Altura_Botador_Inferior_Final', 'Altura_Botador_Superior_Previo', 'Altura_Botador_Superior_Final', 'Altura_Calza_Superior_Trasera',
                  'Altura_Calza_Superior_Izquierda', 'Altura_Calza_Superior_Derecha', 'Altura_Calza_Inferior_Trasera', 'Altura_Calza_Inferior_Izquierda', 'Altura_Calza_Inferior_Derecha',
                  'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
                  'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'] 

@admin.register(Ajuste_forja)
class TerceraTablaAdmin(admin.ModelAdmin):
    list_display = ['folio', 'Inicio', 'Fin',
                  'Altura_Dado_Inferior', 'Altura_Dado_Superior', 'Altura_Calza_Inferior', 'Altura_Calza_Superior', 'Altura_Total',
                  'Altura_Botador_Inferior_Previo', 'Altura_Botador_Inferior_Final', 'Altura_Botador_Superior_Previo', 'Altura_Botador_Superior_Final', 'Altura_Calza_Superior_Trasera',
                  'Altura_Calza_Superior_Izquierda', 'Altura_Calza_Superior_Derecha', 'Altura_Calza_Inferior_Trasera', 'Altura_Calza_Inferior_Izquierda', 'Altura_Calza_Inferior_Derecha',
     ]
    search_fields = ['folio__folio','Inicio', 'Fin',
                  'Altura_Dado_Inferior', 'Altura_Dado_Superior', 'Altura_Calza_Inferior', 'Altura_Calza_Superior', 'Altura_Total',
                  'Altura_Botador_Inferior_Previo', 'Altura_Botador_Inferior_Final', 'Altura_Botador_Superior_Previo', 'Altura_Botador_Superior_Final', 'Altura_Calza_Superior_Trasera',
                  'Altura_Calza_Superior_Izquierda', 'Altura_Calza_Superior_Derecha', 'Altura_Calza_Inferior_Trasera', 'Altura_Calza_Inferior_Izquierda', 'Altura_Calza_Inferior_Derecha',
     ]

@admin.register(Fin_forja)
class CuartaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Altura_Dado_Inferior', 'Altura_Dado_Superior', 'Altura_Calza_Inferior', 'Altura_Calza_Superior', 'Altura_Total',
                  'Altura_Botador_Inferior_Previo', 'Altura_Botador_Inferior_Final', 'Altura_Botador_Superior_Previo', 'Altura_Botador_Superior_Final', 'Altura_Calza_Superior_Trasera',
                  'Altura_Calza_Superior_Izquierda', 'Altura_Calza_Superior_Derecha', 'Altura_Calza_Inferior_Trasera', 'Altura_Calza_Inferior_Izquierda', 'Altura_Calza_Inferior_Derecha',
                   ]
    search_fields = ['folio__folio','Altura_Dado_Inferior', 'Altura_Dado_Superior', 'Altura_Calza_Inferior', 'Altura_Calza_Superior', 'Altura_Total',
                  'Altura_Botador_Inferior_Previo', 'Altura_Botador_Inferior_Final', 'Altura_Botador_Superior_Previo', 'Altura_Botador_Superior_Final', 'Altura_Calza_Superior_Trasera',
                  'Altura_Calza_Superior_Izquierda', 'Altura_Calza_Superior_Derecha', 'Altura_Calza_Inferior_Trasera', 'Altura_Calza_Inferior_Izquierda', 'Altura_Calza_Inferior_Derecha',
                   ]
@admin.register(Registro_recorte)    
class QuintaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Montador', 'Auxiliar', 'Inicio', 'Fin', 'carrera',
            'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
            'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'
                     ]
    search_fields = ['folio__folio','Montador', 'Auxiliar', 'Inicio', 'Fin', 'carrera',
            'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
            'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'
                     ]
@admin.register(Ajuste_recorte)    
class SextaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Inicio', 'Fin', 'carrera']
    search_fields = ['folio__folio', 'Inicio', 'Fin', 'carrera']
@admin.register(Fin_recorte)    
class SeptimaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','carrera']
    search_fields = ['folio__folio','carrera']
@admin.register(Registro_laminado)    
class OctavaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Montador', 'Auxiliar', 'Inicio', 'Fin', 'Holgura',
            'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
            'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'
                    ]
    search_fields = ['folio__folio','Montador', 'Auxiliar', 'Inicio', 'Fin', 'Holgura',
            'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
            'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'
                    ]
@admin.register(Ajuste_laminado)    
class NovenaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Inicio', 'Fin', 'Holgura']
    search_fields = ['folio__folio','Inicio', 'Fin', 'Holgura']
@admin.register(Fin_laminado)    
class DecimaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Holgura']
    search_fields = ['folio__folio','Holgura']
@admin.register(Registro_PP)    
class DecimaprimeraTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Montador', 'Auxiliar', 'Inicio', 'Fin', 'Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza',
                    'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2',
                    'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3', 'Tiempo_muerto_Minutos_3',
                    'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones']
    search_fields = ['folio__folio','Montador', 'Auxiliar', 'Inicio', 'Fin', 'Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza',
                    'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2',
                    'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3', 'Tiempo_muerto_Minutos_3',
                    'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones']
@admin.register(Ajuste_PP)    
class DecimasegundaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Inicio', 'Fin', 'Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza']
    search_fields = ['folio__folio', 'Inicio', 'Fin', 'Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza']
@admin.register(Fin_PP)    
class DecimaterceraTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza']
    search_fields = ['folio__folio','Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza']
@admin.register(Registro_PD)    
class DecimacuartaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Montador', 'Auxiliar', 'Inicio', 'Fin', 'Espesor_Matriz_Izquierda',
                'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza',
                'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2',
                'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3', 'Tiempo_muerto_Minutos_3',
                'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones']
    search_fields = ['folio__folio','Montador', 'Auxiliar', 'Inicio', 'Fin', 'Espesor_Matriz_Izquierda',
                'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza',
                'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2',
                'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3', 'Tiempo_muerto_Minutos_3',
                'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones']
@admin.register(Ajuste_PD)    
class DecimaquintaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio', 'Inicio', 'Fin', 'Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza',
                    ]
    search_fields = ['folio__folio', 'Inicio', 'Fin', 'Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza',
                    ]
@admin.register(Fin_PD)    
class DecimasextaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza']
    search_fields = ['folio__folio','Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza']
@admin.register(Registro_planchado)    
class DecimaseptimaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Montador', 'Auxiliar', 'Inicio', 'Fin', 'carrera',
            'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
            'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'
                     ]
    search_fields = ['folio__folio','Montador', 'Auxiliar', 'Inicio', 'Fin', 'carrera',
            'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
            'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'
                     ]
@admin.register(Ajuste_planchado)    
class DecimaoctavaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Inicio', 'Fin', 'carrera']
    search_fields = ['folio__folio','Inicio', 'Fin', 'carrera']
@admin.register(Fin_planchado)    
class DecimonovenaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','carrera']
    search_fields = ['folio__folio','carrera']
@admin.register(Registro_hs)    
class VigecimaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','Montador', 'Auxiliar', 'Inicio', 'Fin', 'carrera',
            'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
            'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'
                     ]
    search_fields = ['folio__folio','Montador', 'Auxiliar', 'Inicio', 'Fin', 'carrera',
            'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
            'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'
                     ]
@admin.register(Ajuste_hs)    
class VigecimaprimeraTablaAdmin(admin.ModelAdmin):
    list_display = ['folio', 'Inicio', 'Fin', 'carrera']
    search_fields = ['folio__folio', 'Inicio', 'Fin', 'carrera']
@admin.register(Fin_hs)    
class VigecimasegundaTablaAdmin(admin.ModelAdmin):
    list_display = ['folio','carrera']
    search_fields = ['folio__folio','carrera']