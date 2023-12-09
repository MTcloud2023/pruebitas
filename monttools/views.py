from django.shortcuts import get_object_or_404, render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth import login , logout , authenticate
from django.db import IntegrityError
from .forms import *
from .models import*
# Create your views here.
def principal(request):
    return render (request, 'principal.html')
def inicio(request):
    return render (request, 'inicio.html')

def acceso(request):
    if request.method == "GET" :
        return render(request,'acceso.html',{
        'form' : AuthenticationForm
        })
    
    else:
      user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
      if user is None:
        return render(request,'acceso.html',{
        'form' : AuthenticationForm,
        'error' :'Usuario o contraseña incorrectos por favor ingrese los datos nuevamente.'
        })
      else:
          login(request, user)          
          return redirect('inicio')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
        'form': UserCreationForm 
           })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:     
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save
                login(request, user)
                return redirect('acceso')
            except IntegrityError:
                return render(request, 'registro.html', {
                'form': UserCreationForm, 
                'error' : 'usuario ya existe'
                })
                    
        return render(request, 'registro.html', {
                'form': UserCreationForm, 
                'error' : 'Pasword no coincide'
                })
def cerrarsesion(request):
    logout(request)
    return redirect('principal')

def formulario(request):

    
    if request.method == 'GET':
        form_primera_tabla = Datos_Generales_form()
        form_segunda_tabla = Registro_Forja_form()
        form_3_tabla = Registro_ajusteforja_form()
        form_4_tabla = Registro_finforja_form()
        form_5_tabla = Registro_recorte_form()
        form_6_tabla = Registro_ajusterecorte_form()
        form_7_tabla = Registro_finrecorte_form()
        form_8_tabla = Registro_laminado_form()
        form_9_tabla = Registro_ajustelaminado_form()
        form_10_tabla = Registro_finlaminado_form()
        form_11_tabla = Registro_PP_form()
        form_12_tabla = Registro_ajustePP_form()
        form_13_tabla = Registro_finPP_form()
        form_14_tabla = Registro_PD_form()
        form_15_tabla = Registro_ajustePD_form()
        form_16_tabla = Registro_finPD_form()
        form_17_tabla = Registro_planchado_form()
        form_18_tabla = Registro_ajusteplanchado_form()
        form_19_tabla = Registro_finplanchado_form()
        form_20_tabla = Registro_hs_form()
        form_21_tabla = Registro_ajustehs_form()
        form_22_tabla = Registro_finhs_form()       
        return render(request, 'crear_registro.html', {'form_primera_tabla': form_primera_tabla, 'form_segunda_tabla': form_segunda_tabla,
            'form_3_tabla' : form_3_tabla, 'form_4_tabla' : form_4_tabla, 'form_5_tabla' : form_5_tabla, 'form_6_tabla' : form_6_tabla, 
            'form_7_tabla' : form_7_tabla, 'form_8_tabla' : form_8_tabla, 'form_9_tabla' : form_9_tabla, 'form_10_tabla' : form_10_tabla, 
            'form_11_tabla' : form_11_tabla, 'form_12_tabla' : form_12_tabla, 'form_13_tabla' : form_13_tabla, 'form_14_tabla' : form_14_tabla, 'form_15_tabla' : form_15_tabla, 
            'form_16_tabla' : form_16_tabla, 'form_17_tabla' : form_17_tabla, 'form_18_tabla' : form_18_tabla, 'form_19_tabla' : form_19_tabla, 
            'form_20_tabla' : form_20_tabla, 'form_21_tabla' : form_21_tabla, 'form_22_tabla' : form_22_tabla})       
    
    elif request.method == 'POST':
        form_primera_tabla = Datos_Generales_form(request.POST)
        form_segunda_tabla = Registro_Forja_form(request.POST)
        form_3_tabla = Registro_ajusteforja_form(request.POST)
        form_4_tabla = Registro_finforja_form(request.POST)
        form_5_tabla = Registro_recorte_form(request.POST)
        form_6_tabla = Registro_ajusterecorte_form(request.POST)
        form_7_tabla = Registro_finrecorte_form(request.POST)
        form_8_tabla = Registro_laminado_form(request.POST)
        form_9_tabla = Registro_ajustelaminado_form(request.POST)
        form_10_tabla = Registro_finlaminado_form(request.POST)
        form_11_tabla = Registro_PP_form(request.POST)
        form_12_tabla = Registro_ajustePP_form(request.POST)
        form_13_tabla = Registro_finPP_form(request.POST)
        form_14_tabla = Registro_PD_form(request.POST)
        form_15_tabla = Registro_ajustePD_form(request.POST)
        form_16_tabla = Registro_finPD_form(request.POST)
        form_17_tabla = Registro_planchado_form(request.POST)
        form_18_tabla = Registro_ajusteplanchado_form(request.POST)
        form_19_tabla = Registro_finplanchado_form(request.POST)
        form_20_tabla = Registro_hs_form(request.POST)
        form_21_tabla = Registro_ajustehs_form(request.POST)
        form_22_tabla = Registro_finhs_form(request.POST)

        if form_primera_tabla.is_valid() and form_segunda_tabla.is_valid() and form_3_tabla.is_valid() and form_4_tabla.is_valid() and form_5_tabla.is_valid() and form_6_tabla.is_valid() and form_7_tabla.is_valid() and form_8_tabla.is_valid() and form_9_tabla.is_valid() and form_10_tabla.is_valid() and form_11_tabla.is_valid() and form_12_tabla.is_valid() and form_13_tabla.is_valid() and form_14_tabla.is_valid() and form_15_tabla.is_valid() and form_16_tabla.is_valid() and form_17_tabla.is_valid() and form_18_tabla.is_valid() and form_19_tabla.is_valid() and form_20_tabla.is_valid() and form_21_tabla.is_valid() and form_22_tabla.is_valid():           
            primera_tabla = form_primera_tabla.save(commit=False)
            primera_tabla.user = request.user
            primera_tabla.save()

            segunda_tabla = form_segunda_tabla.save(commit=False)
            segunda_tabla.folio = primera_tabla  # Asigna la primera tabla a la segunda
            segunda_tabla.save()

            _3_tabla = form_3_tabla.save(commit=False)
            _3_tabla.folio = primera_tabla
            _3_tabla.save()
            
            _4_tabla = form_4_tabla.save(commit=False)
            _4_tabla.folio = primera_tabla
            _4_tabla.save()
            
            _5_tabla = form_5_tabla.save(commit=False)
            _5_tabla.folio = primera_tabla
            _5_tabla.save()
            
            _6_tabla = form_6_tabla.save(commit=False)
            _6_tabla.folio = primera_tabla
            _6_tabla.save()
            
            _7_tabla = form_7_tabla.save(commit=False)
            _7_tabla.folio = primera_tabla
            _7_tabla.save()
            
            _8_tabla = form_8_tabla.save(commit=False)
            _8_tabla.folio = primera_tabla
            _8_tabla.save()
            
            _9_tabla = form_9_tabla.save(commit=False)
            _9_tabla.folio = primera_tabla
            _9_tabla.save()
            
            _10_tabla = form_10_tabla.save(commit=False)
            _10_tabla.folio = primera_tabla
            _10_tabla.save()
            
            _11_tabla = form_11_tabla.save(commit=False)
            _11_tabla.folio = primera_tabla
            _11_tabla.save()
            
            _12_tabla = form_12_tabla.save(commit=False)
            _12_tabla.folio = primera_tabla
            _12_tabla.save()
            
            _13_tabla = form_13_tabla.save(commit=False)
            _13_tabla.folio = primera_tabla
            _13_tabla.save()
            
            _14_tabla = form_14_tabla.save(commit=False)
            _14_tabla.folio = primera_tabla
            _14_tabla.save()
            
            _15_tabla = form_15_tabla.save(commit=False)
            _15_tabla.folio = primera_tabla
            _15_tabla.save()
            
            _16_tabla = form_16_tabla.save(commit=False)
            _16_tabla.folio = primera_tabla
            _16_tabla.save()
            
            _17_tabla = form_17_tabla.save(commit=False)
            _17_tabla.folio = primera_tabla
            _17_tabla.save()
            
            _18_tabla = form_18_tabla.save(commit=False)
            _18_tabla.folio = primera_tabla
            _18_tabla.save()
            
            _19_tabla = form_19_tabla.save(commit=False)
            _19_tabla.folio = primera_tabla
            _19_tabla.save()
            
            _20_tabla = form_20_tabla.save(commit=False)
            _20_tabla.folio = primera_tabla
            _20_tabla.save()
            
            _21_tabla = form_21_tabla.save(commit=False)
            _21_tabla.folio = primera_tabla
            _21_tabla.save()
            
            _22_tabla = form_22_tabla.save(commit=False)
            _22_tabla.folio = primera_tabla
            _22_tabla.save()

            return redirect('inicio')
    else:
        form_primera_tabla = Datos_Generales_form()
        form_segunda_tabla = Registro_Forja_form()
        form_3_tabla = Registro_ajusteforja_form()
        form_4_tabla = Registro_finforja_form()
        form_5_tabla = Registro_recorte_form()
        form_6_tabla = Registro_ajusterecorte_form()
        form_7_tabla = Registro_finrecorte_form()
        form_8_tabla = Registro_laminado_form()
        form_9_tabla = Registro_ajustelaminado_form()
        form_10_tabla = Registro_finlaminado_form()
        form_11_tabla = Registro_PP_form()
        form_12_tabla = Registro_ajustePP_form()
        form_13_tabla = Registro_finPP_form()
        form_14_tabla = Registro_PD_form()
        form_15_tabla = Registro_ajustePD_form()
        form_16_tabla = Registro_finPD_form()
        form_17_tabla = Registro_planchado_form()
        form_18_tabla = Registro_ajusteplanchado_form()
        form_19_tabla = Registro_finplanchado_form()
        form_20_tabla = Registro_hs_form()
        form_21_tabla = Registro_ajustehs_form()
        form_22_tabla = Registro_finhs_form()        

    return render(request, 'crear_registro.html', {'form_primera_tabla': form_primera_tabla, 'form_segunda_tabla': form_segunda_tabla,
         'form_3_tabla' : form_3_tabla, 'form_4_tabla' : form_4_tabla, 'form_5_tabla' : form_5_tabla, 'form_6_tabla' : form_6_tabla, 
         'form_7_tabla' : form_7_tabla, 'form_8_tabla' : form_8_tabla, 'form_9_tabla' : form_9_tabla, 'form_10_tabla' : form_10_tabla, 
         'form_11_tabla' : form_11_tabla, 'form_12_tabla' : form_12_tabla, 'form_13_tabla' : form_13_tabla, 'form_14_tabla' : form_14_tabla, 'form_15_tabla' : form_15_tabla, 
         'form_16_tabla' : form_16_tabla, 'form_17_tabla' : form_17_tabla, 'form_18_tabla' : form_18_tabla, 'form_19_tabla' : form_19_tabla, 
         'form_20_tabla' : form_20_tabla, 'form_21_tabla' : form_21_tabla, 'form_22_tabla' : form_22_tabla})

def consulta_datos(request):
    primera_tabla_data =  datos_principales.objects.all()
    segunda_tabla_data = Registro_forja.objects.all()
    _3_tabla_data = Ajuste_forja.objects.all()
    _4_tabla_data = Fin_forja.objects.all()
    _5_tabla_data = Registro_recorte.objects.all()
    _6_tabla_data = Ajuste_recorte.objects.all()
    _7_tabla_data = Fin_recorte.objects.all()
    _8_tabla_data = Registro_laminado.objects.all()
    _9_tabla_data = Ajuste_laminado.objects.all()
    _10_tabla_data = Fin_laminado.objects.all()
    _11_tabla_data = Registro_PP.objects.all()
    _12_tabla_data = Ajuste_PP.objects.all()
    _13_tabla_data = Fin_PP.objects.all()
    _14_tabla_data = Registro_PD.objects.all()
    _15_tabla_data = Ajuste_PD.objects.all()
    _16_tabla_data = Fin_PD.objects.all()
    _17_tabla_data = Registro_planchado.objects.all()
    _18_tabla_data = Ajuste_planchado.objects.all()
    _19_tabla_data = Fin_planchado.objects.all()
    _20_tabla_data = Registro_hs.objects.all()
    _21_tabla_data = Ajuste_hs.objects.all()
    _22_tabla_data = Fin_hs.objects.all()


    return render(request, 'consulta_datos.html', {'primera_tabla_data': primera_tabla_data, 'segunda_tabla_data': segunda_tabla_data,
    '3_tabla_data' : _3_tabla_data,'4_tabla_data' : _4_tabla_data,'5_tabla_data' : _5_tabla_data,'6_tabla_data' : _6_tabla_data,'7_tabla_data' : _7_tabla_data,
    '8_tabla_data' : _8_tabla_data,'9_tabla_data' : _9_tabla_data,'10_tabla_data' : _10_tabla_data,'11_tabla_data' : _11_tabla_data,'12_tabla_data' : _12_tabla_data,
    '13_tabla_data' : _13_tabla_data,'14_tabla_data' : _14_tabla_data,'15_tabla_data' : _15_tabla_data,'16_tabla_data' : _16_tabla_data,'17_tabla_data' : _17_tabla_data,
    '18_tabla_data' : _18_tabla_data,'19_tabla_data' : _19_tabla_data,'20_tabla_data' : _20_tabla_data,'21_tabla_data' : _21_tabla_data,'22_tabla_data' : _22_tabla_data })

def detalle(request):
    primera_tabla_data =  datos_principales.objects.all()


    return render(request, 'detalle_data.html',{'primera_tabla_data': primera_tabla_data})

def adetalle(request,folio_id):
    # Obtener el elemento específico de datos_principales
    elemento_datos_principales = datos_principales.objects.get(folio=folio_id)

    # Obtener elementos relacionados de otras tablas usando la clave foránea
    segunda_tabla_data = Registro_forja.objects.filter(folio=elemento_datos_principales.folio)
    _3_tabla_data = Ajuste_forja.objects.filter(folio=elemento_datos_principales.folio)
    _4_tabla_data = Fin_forja.objects.filter(folio=elemento_datos_principales.folio)
    _5_tabla_data = Registro_recorte.objects.filter(folio=elemento_datos_principales.folio)
    _6_tabla_data = Ajuste_recorte.objects.filter(folio=elemento_datos_principales.folio)
    _7_tabla_data = Fin_recorte.objects.filter(folio=elemento_datos_principales.folio)
    _8_tabla_data = Registro_laminado.objects.filter(folio=elemento_datos_principales.folio)
    _9_tabla_data = Ajuste_laminado.objects.filter(folio=elemento_datos_principales.folio)
    _10_tabla_data = Fin_laminado.objects.filter(folio=elemento_datos_principales.folio)
    _11_tabla_data = Registro_PP.objects.filter(folio=elemento_datos_principales.folio)
    _12_tabla_data = Ajuste_PP.objects.filter(folio=elemento_datos_principales.folio)
    _13_tabla_data = Fin_PP.objects.filter(folio=elemento_datos_principales.folio)
    _14_tabla_data = Registro_PD.objects.filter(folio=elemento_datos_principales.folio)
    _15_tabla_data = Ajuste_PD.objects.filter(folio=elemento_datos_principales.folio)
    _16_tabla_data = Fin_PD.objects.filter(folio=elemento_datos_principales.folio)
    _17_tabla_data = Registro_planchado.objects.filter(folio=elemento_datos_principales.folio)
    _18_tabla_data = Ajuste_planchado.objects.filter(folio=elemento_datos_principales.folio)
    _19_tabla_data = Fin_planchado.objects.filter(folio=elemento_datos_principales.folio)
    _20_tabla_data = Registro_hs.objects.filter(folio=elemento_datos_principales.folio)
    _21_tabla_data = Ajuste_hs.objects.filter(folio=elemento_datos_principales.folio)
    _22_tabla_data = Fin_hs.objects.filter(folio=elemento_datos_principales.folio)

    # Repite este proceso para las demás tablas

    return render(request, 'especifico.html', {
        'elemento_datos_principales': elemento_datos_principales,
        'segunda_tabla_data': segunda_tabla_data,
        '3_tabla_data' : _3_tabla_data,'4_tabla_data' : _4_tabla_data,'5_tabla_data' : _5_tabla_data,'6_tabla_data' : _6_tabla_data,'7_tabla_data' : _7_tabla_data,
        '8_tabla_data' : _8_tabla_data,'9_tabla_data' : _9_tabla_data,'10_tabla_data' : _10_tabla_data,'11_tabla_data' : _11_tabla_data,'12_tabla_data' : _12_tabla_data,
        '13_tabla_data' : _13_tabla_data,'14_tabla_data' : _14_tabla_data,'15_tabla_data' : _15_tabla_data,'16_tabla_data' : _16_tabla_data,'17_tabla_data' : _17_tabla_data,
        '18_tabla_data' : _18_tabla_data,'19_tabla_data' : _19_tabla_data,'20_tabla_data' : _20_tabla_data,'21_tabla_data' : _21_tabla_data,'22_tabla_data' : _22_tabla_data})



  

        