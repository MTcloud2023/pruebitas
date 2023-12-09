from django import forms 
from .models import *
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','important']

class Datos_Generales_form(forms.ModelForm):
    class Meta:
        model = datos_principales
        fields = ['folio','centro','modelo_anterior','modelo_actual','fecha','hora_ot','cambio_programado']

class Centros_form(forms.ModelForm):
    class Meta:
        model = Centros
        fields = ['Area','forja']

class Producto_form(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['modelo']

class Registro_Forja_form(forms.ModelForm):
    class Meta:
        model = Registro_forja
        fields =['Montador', 'Auxiliar', 'Inicio', 'Fin',
                  'Altura_Dado_Inferior', 'Altura_Dado_Superior', 'Altura_Calza_Inferior', 'Altura_Calza_Superior', 'Altura_Total',
                  'Altura_Botador_Inferior_Previo', 'Altura_Botador_Inferior_Final', 'Altura_Botador_Superior_Previo', 'Altura_Botador_Superior_Final', 'Altura_Calza_Superior_Trasera',
                  'Altura_Calza_Superior_Izquierda', 'Altura_Calza_Superior_Derecha', 'Altura_Calza_Inferior_Trasera', 'Altura_Calza_Inferior_Izquierda', 'Altura_Calza_Inferior_Derecha',
                  'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
                  'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones']
        
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()

class Registro_ajusteforja_form(forms.ModelForm):
    class Meta:
        model = Ajuste_forja
        fields =['Inicio', 'Fin',
                  'Altura_Dado_Inferior', 'Altura_Dado_Superior', 'Altura_Calza_Inferior', 'Altura_Calza_Superior', 'Altura_Total',
                  'Altura_Botador_Inferior_Previo', 'Altura_Botador_Inferior_Final', 'Altura_Botador_Superior_Previo', 'Altura_Botador_Superior_Final', 'Altura_Calza_Superior_Trasera',
                  'Altura_Calza_Superior_Izquierda', 'Altura_Calza_Superior_Derecha', 'Altura_Calza_Inferior_Trasera', 'Altura_Calza_Inferior_Izquierda', 'Altura_Calza_Inferior_Derecha',
                ]
        
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()
class Registro_finforja_form(forms.ModelForm):
     class Meta:
        model = Fin_forja
        fields =[
                  'Altura_Dado_Inferior', 'Altura_Dado_Superior', 'Altura_Calza_Inferior', 'Altura_Calza_Superior', 'Altura_Total',
                  'Altura_Botador_Inferior_Previo', 'Altura_Botador_Inferior_Final', 'Altura_Botador_Superior_Previo', 'Altura_Botador_Superior_Final', 'Altura_Calza_Superior_Trasera',
                  'Altura_Calza_Superior_Izquierda', 'Altura_Calza_Superior_Derecha', 'Altura_Calza_Inferior_Trasera', 'Altura_Calza_Inferior_Izquierda', 'Altura_Calza_Inferior_Derecha',
                    ]
        
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()    
class Registro_recorte_form(forms.ModelForm):
     class Meta:
          model =Registro_recorte
          fields = ['Montador', 'Auxiliar', 'Inicio', 'Fin', 'carrera',
            'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
            'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'
                     ]
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()    
class Registro_ajusterecorte_form(forms.ModelForm): 
     class Meta:
          model = Ajuste_recorte
          fields = ['Inicio', 'Fin', 'carrera'] 
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()                     
class Registro_finrecorte_form(forms.ModelForm):
     class Meta:
          model = Fin_recorte
          fields = ['carrera']
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()              
class Registro_laminado_form(forms.ModelForm):
     class Meta:
          model = Registro_laminado
          fields = ['Montador', 'Auxiliar', 'Inicio', 'Fin', 'Holgura',
            'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
            'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'
                     ]
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()              

class Registro_ajustelaminado_form(forms.ModelForm): 
     class Meta:
          model =Ajuste_laminado
          fields = ['Inicio', 'Fin', 'Holgura']  
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()              
class Registro_finlaminado_form(forms.ModelForm):
     class Meta:
          model =Fin_laminado
          fields = ['Holgura'] 
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()  

class Registro_PP_form(forms.ModelForm):    
     class Meta:
          model = Registro_PP
          fields = ['Montador', 'Auxiliar', 'Inicio', 'Fin', 'Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza',
                    'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2',
                    'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3', 'Tiempo_muerto_Minutos_3',
                    'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones']
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()             
class Registro_ajustePP_form(forms.ModelForm):
     class Meta:
          model = Ajuste_PP
          fields = ['Inicio', 'Fin', 'Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza'] 
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()            
class Registro_finPP_form(forms.ModelForm):
     class Meta:
          model = Fin_PP
          fields = ['Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza'] 
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()            
class Registro_PD_form(forms.ModelForm):    
     class Meta:
          model = Registro_PD
          fields = ['Montador', 'Auxiliar', 'Inicio', 'Fin', 'Espesor_Matriz_Izquierda',
                'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza',
                'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2',
                'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3', 'Tiempo_muerto_Minutos_3',
                'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'] 
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()            
class Registro_ajustePD_form(forms.ModelForm):
     class Meta:
          model =Ajuste_PD
          fields = ['Inicio', 'Fin', 'Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza',
                    ] 
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()            
class Registro_finPD_form(forms.ModelForm):    
     class Meta:
          model =Fin_PD
          fields = ['Espesor_Matriz_Izquierda',
                    'Calza_Matriz_Izquierda', 'Espesor_Matriz_Derecha', 'Calza_Matriz_Derecha',
                    'Altura_Punzon', 'Altura_Asiento', 'Calza_en_Asiento', 'Carrera_o_Calza'] 
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()            
class Registro_planchado_form(forms.ModelForm):
     class Meta:
          model = Registro_planchado
          fields = ['Montador', 'Auxiliar', 'Inicio', 'Fin', 'carrera',
            'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
            'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'
                     ] 
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()            
class Registro_ajusteplanchado_form(forms.ModelForm):
     class Meta:
          model = Ajuste_planchado
          fields = ['Inicio', 'Fin', 'carrera'] 
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()            
class Registro_finplanchado_form(forms.ModelForm):  
     class Meta:
          model = Fin_planchado
          fields = [ 'carrera']   
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()            
class Registro_hs_form(forms.ModelForm):
     class Meta:
          model =Registro_hs
          fields = ['Montador', 'Auxiliar', 'Inicio', 'Fin', 'carrera',
            'Tiempo_muerto_Codigo_1', 'Tiempo_muerto_Minutos_1', 'Tiempo_muerto_Codigo_2', 'Tiempo_muerto_Minutos_2', 'Tiempo_muerto_Codigo_3',
            'Tiempo_muerto_Minutos_3', 'Tiempo_muerto_Codigo_4', 'Tiempo_muerto_Minutos_4', 'Observaciones'
                     ] 
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()  

class Registro_ajustehs_form(forms.ModelForm):   
     class Meta:
          model =Ajuste_hs
          fields = ['Inicio', 'Fin', 'carrera']
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()  

class Registro_finhs_form(forms.ModelForm):  
     class Meta:
          model =Fin_hs
          fields = ['carrera']            
          def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Configura el widget del campo 'folio' como TextInput solo si ya existe en el formulario
                if 'folio' in self.fields:
                    self.fields['folio'].widget = forms.TextInput()            