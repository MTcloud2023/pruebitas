from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)  
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True , blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self): 
        return self.title + ' -by ' + self.user.username

class datos_principales(models.Model):
    folio = models.CharField(max_length=100,primary_key=True)
    hora_ot = models.TimeField()
    centro = models.ForeignKey('Centros', on_delete=models.DO_NOTHING)
    modelo_anterior = models.ForeignKey('Productos', related_name='modelo_anterior', on_delete=models.DO_NOTHING)
    modelo_actual = models.ForeignKey('Productos', related_name='modelo_actual', on_delete=models.DO_NOTHING)
    cambio_programado = models.BooleanField(default=False)
    fecha = models.DateField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    creado = models.DateTimeField(auto_now_add=True) 
    def __str__(self): 
        return self.folio

class Centros(models.Model):
    Area = models.CharField(max_length=100)
    forja = models.CharField(max_length=100)
    recorte = models.CharField(max_length=100)
    laminado = models.CharField(max_length=100)
    punzonado_previo = models.CharField(max_length=100)
    punzonado_definitivo = models.CharField(max_length=100)
    planchado = models.CharField(max_length=100)
    habilitado_de_solera = models.CharField(max_length=100)
    def __str__(self): 
        return self.Area
class Productos(models.Model):
    modelo = models.CharField(max_length=100)
    def __str__(self): 
        return self.modelo
class Registro_forja(models.Model):
   
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Montador = models.CharField(max_length=100)
    Auxiliar = models.CharField(max_length=100)
    Inicio = models.TimeField()
    Fin = models.TimeField()
    Altura_Dado_Inferior = models.CharField(max_length=100)
    Altura_Dado_Superior = models.CharField(max_length=100)
    Altura_Calza_Inferior  = models.CharField(max_length=100)
    Altura_Calza_Superior = models.CharField(max_length=100)
    Altura_Total = models.CharField(max_length=100)
    Altura_Botador_Inferior_Previo = models.CharField(max_length=100)
    Altura_Botador_Inferior_Final = models.CharField(max_length=100)
    Altura_Botador_Superior_Previo = models.CharField(max_length=100)
    Altura_Botador_Superior_Final = models.CharField(max_length=100)
    Altura_Calza_Superior_Trasera = models.CharField(max_length=100)
    Altura_Calza_Superior_Izquierda = models.CharField(max_length=100)
    Altura_Calza_Superior_Derecha = models.CharField(max_length=100)
    Altura_Calza_Inferior_Trasera = models.CharField(max_length=100)
    Altura_Calza_Inferior_Izquierda = models.CharField(max_length=100)
    Altura_Calza_Inferior_Derecha = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_1 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_1 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_2 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_2 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_3 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_3 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_4 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_4 = models.CharField(max_length=100)
    Observaciones = models.TextField(blank=True)

class Ajuste_forja(models.Model):
   
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Inicio  = models.TimeField()
    Fin = models.TimeField()
    Altura_Dado_Inferior = models.CharField(max_length=100)
    Altura_Dado_Superior = models.CharField(max_length=100)
    Altura_Calza_Inferior  = models.CharField(max_length=100)
    Altura_Calza_Superior = models.CharField(max_length=100)
    Altura_Total = models.CharField(max_length=100)
    Altura_Botador_Inferior_Previo = models.CharField(max_length=100)
    Altura_Botador_Inferior_Final = models.CharField(max_length=100)
    Altura_Botador_Superior_Previo = models.CharField(max_length=100)
    Altura_Botador_Superior_Final = models.CharField(max_length=100)
    Altura_Calza_Superior_Trasera = models.CharField(max_length=100)
    Altura_Calza_Superior_Izquierda = models.CharField(max_length=100)
    Altura_Calza_Superior_Derecha = models.CharField(max_length=100)
    Altura_Calza_Inferior_Trasera = models.CharField(max_length=100)
    Altura_Calza_Inferior_Izquierda = models.CharField(max_length=100)
    Altura_Calza_Inferior_Derecha = models.CharField(max_length=100)


class Fin_forja(models.Model):
   
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Altura_Dado_Inferior = models.CharField(max_length=100)
    Altura_Dado_Superior = models.CharField(max_length=100)
    Altura_Calza_Inferior  = models.CharField(max_length=100)
    Altura_Calza_Superior = models.CharField(max_length=100)
    Altura_Total = models.CharField(max_length=100)
    Altura_Botador_Inferior_Previo = models.CharField(max_length=100)
    Altura_Botador_Inferior_Final = models.CharField(max_length=100)
    Altura_Botador_Superior_Previo = models.CharField(max_length=100)
    Altura_Botador_Superior_Final = models.CharField(max_length=100)
    Altura_Calza_Superior_Trasera = models.CharField(max_length=100)
    Altura_Calza_Superior_Izquierda = models.CharField(max_length=100)
    Altura_Calza_Superior_Derecha = models.CharField(max_length=100)
    Altura_Calza_Inferior_Trasera = models.CharField(max_length=100)
    Altura_Calza_Inferior_Izquierda = models.CharField(max_length=100)
    Altura_Calza_Inferior_Derecha = models.CharField(max_length=100)

class Registro_recorte(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Montador = models.CharField(max_length=100)
    Auxiliar =models.CharField(max_length=100)
    Inicio = models.TimeField()
    Fin = models.TimeField()
    carrera = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_1 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_1 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_2 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_2 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_3 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_3 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_4 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_4 = models.CharField(max_length=100)
    Observaciones = models.TextField(blank=True)
class Ajuste_recorte(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Inicio = models.TimeField()
    Fin = models.TimeField()
    carrera = models.CharField(max_length=100)

class Fin_recorte(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    carrera = models.CharField(max_length=100)

class Registro_laminado(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Montador = models.CharField(max_length=100)
    Auxiliar =models.CharField(max_length=100)
    Inicio = models.TimeField()
    Fin = models.TimeField()
    Holgura = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_1 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_1 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_2 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_2 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_3 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_3 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_4 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_4 = models.CharField(max_length=100)
    Observaciones = models.TextField(blank=True)

class Ajuste_laminado(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Inicio = models.TimeField()
    Fin = models.TimeField()
    Holgura = models.CharField(max_length=100)

class Fin_laminado(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Holgura = models.CharField(max_length=100)

class Registro_PP(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Montador = models.CharField(max_length=100)
    Auxiliar =models.CharField(max_length=100)
    Inicio = models.TimeField()
    Fin = models.TimeField()    
    Espesor_Matriz_Izquierda = models.CharField(max_length=100)
    Calza_Matriz_Izquierda = models.CharField(max_length=100)
    Espesor_Matriz_Derecha = models.CharField(max_length=100)
    Calza_Matriz_Derecha = models.CharField(max_length=100)
    Altura_Punzon = models.CharField(max_length=100)
    Altura_Asiento = models.CharField(max_length=100)
    Calza_en_Asiento = models.CharField(max_length=100)
    Carrera_o_Calza = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_1 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_1 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_2 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_2 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_3 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_3 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_4 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_4 = models.CharField(max_length=100)
    Observaciones = models.TextField(blank=True)    

class Ajuste_PP(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Inicio = models.TimeField()
    Fin = models.TimeField()    
    Espesor_Matriz_Izquierda = models.CharField(max_length=100)
    Calza_Matriz_Izquierda = models.CharField(max_length=100)
    Espesor_Matriz_Derecha = models.CharField(max_length=100)
    Calza_Matriz_Derecha = models.CharField(max_length=100)
    Altura_Punzon = models.CharField(max_length=100)
    Altura_Asiento = models.CharField(max_length=100)
    Calza_en_Asiento = models.CharField(max_length=100)
    Carrera_o_Calza = models.CharField(max_length=100)
    
class Fin_PP(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Espesor_Matriz_Izquierda = models.CharField(max_length=100)
    Calza_Matriz_Izquierda = models.CharField(max_length=100)
    Espesor_Matriz_Derecha = models.CharField(max_length=100)
    Calza_Matriz_Derecha = models.CharField(max_length=100)
    Altura_Punzon = models.CharField(max_length=100)
    Altura_Asiento = models.CharField(max_length=100)
    Calza_en_Asiento = models.CharField(max_length=100)
    Carrera_o_Calza = models.CharField(max_length=100)
    

class Registro_PD(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Montador = models.CharField(max_length=100)
    Auxiliar =models.CharField(max_length=100)
    Inicio = models.TimeField()
    Fin = models.TimeField()    
    Espesor_Matriz_Izquierda = models.CharField(max_length=100)
    Calza_Matriz_Izquierda = models.CharField(max_length=100)
    Espesor_Matriz_Derecha = models.CharField(max_length=100)
    Calza_Matriz_Derecha = models.CharField(max_length=100)
    Altura_Punzon = models.CharField(max_length=100)
    Altura_Asiento = models.CharField(max_length=100)
    Calza_en_Asiento = models.CharField(max_length=100)
    Carrera_o_Calza = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_1 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_1 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_2 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_2 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_3 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_3 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_4 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_4 = models.CharField(max_length=100)
    Observaciones = models.TextField(blank=True)    
class Ajuste_PD(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Inicio = models.TimeField()
    Fin = models.TimeField()    
    Espesor_Matriz_Izquierda = models.CharField(max_length=100)
    Calza_Matriz_Izquierda = models.CharField(max_length=100)
    Espesor_Matriz_Derecha = models.CharField(max_length=100)
    Calza_Matriz_Derecha = models.CharField(max_length=100)
    Altura_Punzon = models.CharField(max_length=100)
    Altura_Asiento = models.CharField(max_length=100)
    Calza_en_Asiento = models.CharField(max_length=100)
    Carrera_o_Calza = models.CharField(max_length=100)
      
class Fin_PD(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Espesor_Matriz_Izquierda = models.CharField(max_length=100)
    Calza_Matriz_Izquierda = models.CharField(max_length=100)
    Espesor_Matriz_Derecha = models.CharField(max_length=100)
    Calza_Matriz_Derecha = models.CharField(max_length=100)
    Altura_Punzon = models.CharField(max_length=100)
    Altura_Asiento = models.CharField(max_length=100)
    Calza_en_Asiento = models.CharField(max_length=100)
    Carrera_o_Calza = models.CharField(max_length=100)
     

class Registro_planchado(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Montador = models.CharField(max_length=100)
    Auxiliar =models.CharField(max_length=100)
    Inicio = models.TimeField()
    Fin = models.TimeField()
    carrera = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_1 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_1 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_2 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_2 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_3 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_3 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_4 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_4 = models.CharField(max_length=100)
    Observaciones = models.TextField(blank=True)

class Ajuste_planchado(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Inicio = models.TimeField()
    Fin = models.TimeField()
    carrera = models.CharField(max_length=100)

class Fin_planchado(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    carrera = models.CharField(max_length=100)

class Registro_hs(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Montador = models.CharField(max_length=100)
    Auxiliar =models.CharField(max_length=100)
    Inicio = models.TimeField()
    Fin = models.TimeField()
    carrera = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_1 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_1 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_2 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_2 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_3 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_3 = models.CharField(max_length=100)
    Tiempo_muerto_Codigo_4 = models.CharField(max_length=100)
    Tiempo_muerto_Minutos_4 = models.CharField(max_length=100)
    Observaciones = models.TextField(blank=True)

class Ajuste_hs(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    Inicio = models.TimeField()
    Fin = models.TimeField()
    carrera = models.CharField(max_length=100)

class Fin_hs(models.Model):
    folio = models.ForeignKey(datos_principales,on_delete=models.CASCADE)
    carrera = models.CharField(max_length=100)
