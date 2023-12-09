# Generated by Django 4.2.8 on 2023-12-09 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Centros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area', models.CharField(max_length=100)),
                ('forja', models.CharField(max_length=100)),
                ('recorte', models.CharField(max_length=100)),
                ('laminado', models.CharField(max_length=100)),
                ('punzonado_previo', models.CharField(max_length=100)),
                ('punzonado_definitivo', models.CharField(max_length=100)),
                ('planchado', models.CharField(max_length=100)),
                ('habilitado_de_solera', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='datos_principales',
            fields=[
                ('folio', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('hora_ot', models.TimeField()),
                ('cambio_programado', models.BooleanField(default=False)),
                ('fecha', models.DateField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='monttools.centros')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datecompleted', models.DateTimeField(blank=True, null=True)),
                ('important', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registro_recorte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Montador', models.CharField(max_length=100)),
                ('Auxiliar', models.CharField(max_length=100)),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('carrera', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_4', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_4', models.CharField(max_length=100)),
                ('Observaciones', models.TextField(blank=True)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Registro_PP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Montador', models.CharField(max_length=100)),
                ('Auxiliar', models.CharField(max_length=100)),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('Espesor_Matriz_Izquierda', models.CharField(max_length=100)),
                ('Calza_Matriz_Izquierda', models.CharField(max_length=100)),
                ('Espesor_Matriz_Derecha', models.CharField(max_length=100)),
                ('Calza_Matriz_Derecha', models.CharField(max_length=100)),
                ('Altura_Punzon', models.CharField(max_length=100)),
                ('Altura_Asiento', models.CharField(max_length=100)),
                ('Calza_en_Asiento', models.CharField(max_length=100)),
                ('Carrera_o_Calza', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_4', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_4', models.CharField(max_length=100)),
                ('Observaciones', models.TextField(blank=True)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Registro_planchado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Montador', models.CharField(max_length=100)),
                ('Auxiliar', models.CharField(max_length=100)),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('carrera', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_4', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_4', models.CharField(max_length=100)),
                ('Observaciones', models.TextField(blank=True)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Registro_PD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Montador', models.CharField(max_length=100)),
                ('Auxiliar', models.CharField(max_length=100)),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('Espesor_Matriz_Izquierda', models.CharField(max_length=100)),
                ('Calza_Matriz_Izquierda', models.CharField(max_length=100)),
                ('Espesor_Matriz_Derecha', models.CharField(max_length=100)),
                ('Calza_Matriz_Derecha', models.CharField(max_length=100)),
                ('Altura_Punzon', models.CharField(max_length=100)),
                ('Altura_Asiento', models.CharField(max_length=100)),
                ('Calza_en_Asiento', models.CharField(max_length=100)),
                ('Carrera_o_Calza', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_4', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_4', models.CharField(max_length=100)),
                ('Observaciones', models.TextField(blank=True)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Registro_laminado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Montador', models.CharField(max_length=100)),
                ('Auxiliar', models.CharField(max_length=100)),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('Holgura', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_4', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_4', models.CharField(max_length=100)),
                ('Observaciones', models.TextField(blank=True)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Registro_hs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Montador', models.CharField(max_length=100)),
                ('Auxiliar', models.CharField(max_length=100)),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('carrera', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_4', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_4', models.CharField(max_length=100)),
                ('Observaciones', models.TextField(blank=True)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Registro_forja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Montador', models.CharField(max_length=100)),
                ('Auxiliar', models.CharField(max_length=100)),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('Altura_Dado_Inferior', models.CharField(max_length=100)),
                ('Altura_Dado_Superior', models.CharField(max_length=100)),
                ('Altura_Calza_Inferior', models.CharField(max_length=100)),
                ('Altura_Calza_Superior', models.CharField(max_length=100)),
                ('Altura_Total', models.CharField(max_length=100)),
                ('Altura_Botador_Inferior_Previo', models.CharField(max_length=100)),
                ('Altura_Botador_Inferior_Final', models.CharField(max_length=100)),
                ('Altura_Botador_Superior_Previo', models.CharField(max_length=100)),
                ('Altura_Botador_Superior_Final', models.CharField(max_length=100)),
                ('Altura_Calza_Superior_Trasera', models.CharField(max_length=100)),
                ('Altura_Calza_Superior_Izquierda', models.CharField(max_length=100)),
                ('Altura_Calza_Superior_Derecha', models.CharField(max_length=100)),
                ('Altura_Calza_Inferior_Trasera', models.CharField(max_length=100)),
                ('Altura_Calza_Inferior_Izquierda', models.CharField(max_length=100)),
                ('Altura_Calza_Inferior_Derecha', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_1', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_2', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_3', models.CharField(max_length=100)),
                ('Tiempo_muerto_Codigo_4', models.CharField(max_length=100)),
                ('Tiempo_muerto_Minutos_4', models.CharField(max_length=100)),
                ('Observaciones', models.TextField(blank=True)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_recorte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrera', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_PP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Espesor_Matriz_Izquierda', models.CharField(max_length=100)),
                ('Calza_Matriz_Izquierda', models.CharField(max_length=100)),
                ('Espesor_Matriz_Derecha', models.CharField(max_length=100)),
                ('Calza_Matriz_Derecha', models.CharField(max_length=100)),
                ('Altura_Punzon', models.CharField(max_length=100)),
                ('Altura_Asiento', models.CharField(max_length=100)),
                ('Calza_en_Asiento', models.CharField(max_length=100)),
                ('Carrera_o_Calza', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_planchado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrera', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_PD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Espesor_Matriz_Izquierda', models.CharField(max_length=100)),
                ('Calza_Matriz_Izquierda', models.CharField(max_length=100)),
                ('Espesor_Matriz_Derecha', models.CharField(max_length=100)),
                ('Calza_Matriz_Derecha', models.CharField(max_length=100)),
                ('Altura_Punzon', models.CharField(max_length=100)),
                ('Altura_Asiento', models.CharField(max_length=100)),
                ('Calza_en_Asiento', models.CharField(max_length=100)),
                ('Carrera_o_Calza', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_laminado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Holgura', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_hs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrera', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_forja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Altura_Dado_Inferior', models.CharField(max_length=100)),
                ('Altura_Dado_Superior', models.CharField(max_length=100)),
                ('Altura_Calza_Inferior', models.CharField(max_length=100)),
                ('Altura_Calza_Superior', models.CharField(max_length=100)),
                ('Altura_Total', models.CharField(max_length=100)),
                ('Altura_Botador_Inferior_Previo', models.CharField(max_length=100)),
                ('Altura_Botador_Inferior_Final', models.CharField(max_length=100)),
                ('Altura_Botador_Superior_Previo', models.CharField(max_length=100)),
                ('Altura_Botador_Superior_Final', models.CharField(max_length=100)),
                ('Altura_Calza_Superior_Trasera', models.CharField(max_length=100)),
                ('Altura_Calza_Superior_Izquierda', models.CharField(max_length=100)),
                ('Altura_Calza_Superior_Derecha', models.CharField(max_length=100)),
                ('Altura_Calza_Inferior_Trasera', models.CharField(max_length=100)),
                ('Altura_Calza_Inferior_Izquierda', models.CharField(max_length=100)),
                ('Altura_Calza_Inferior_Derecha', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.AddField(
            model_name='datos_principales',
            name='modelo_actual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='modelo_actual', to='monttools.productos'),
        ),
        migrations.AddField(
            model_name='datos_principales',
            name='modelo_anterior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='modelo_anterior', to='monttools.productos'),
        ),
        migrations.AddField(
            model_name='datos_principales',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Ajuste_recorte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('carrera', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Ajuste_PP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('Espesor_Matriz_Izquierda', models.CharField(max_length=100)),
                ('Calza_Matriz_Izquierda', models.CharField(max_length=100)),
                ('Espesor_Matriz_Derecha', models.CharField(max_length=100)),
                ('Calza_Matriz_Derecha', models.CharField(max_length=100)),
                ('Altura_Punzon', models.CharField(max_length=100)),
                ('Altura_Asiento', models.CharField(max_length=100)),
                ('Calza_en_Asiento', models.CharField(max_length=100)),
                ('Carrera_o_Calza', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Ajuste_planchado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('carrera', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Ajuste_PD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('Espesor_Matriz_Izquierda', models.CharField(max_length=100)),
                ('Calza_Matriz_Izquierda', models.CharField(max_length=100)),
                ('Espesor_Matriz_Derecha', models.CharField(max_length=100)),
                ('Calza_Matriz_Derecha', models.CharField(max_length=100)),
                ('Altura_Punzon', models.CharField(max_length=100)),
                ('Altura_Asiento', models.CharField(max_length=100)),
                ('Calza_en_Asiento', models.CharField(max_length=100)),
                ('Carrera_o_Calza', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Ajuste_laminado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('Holgura', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Ajuste_hs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('carrera', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
        migrations.CreateModel(
            name='Ajuste_forja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Inicio', models.TimeField()),
                ('Fin', models.TimeField()),
                ('Altura_Dado_Inferior', models.CharField(max_length=100)),
                ('Altura_Dado_Superior', models.CharField(max_length=100)),
                ('Altura_Calza_Inferior', models.CharField(max_length=100)),
                ('Altura_Calza_Superior', models.CharField(max_length=100)),
                ('Altura_Total', models.CharField(max_length=100)),
                ('Altura_Botador_Inferior_Previo', models.CharField(max_length=100)),
                ('Altura_Botador_Inferior_Final', models.CharField(max_length=100)),
                ('Altura_Botador_Superior_Previo', models.CharField(max_length=100)),
                ('Altura_Botador_Superior_Final', models.CharField(max_length=100)),
                ('Altura_Calza_Superior_Trasera', models.CharField(max_length=100)),
                ('Altura_Calza_Superior_Izquierda', models.CharField(max_length=100)),
                ('Altura_Calza_Superior_Derecha', models.CharField(max_length=100)),
                ('Altura_Calza_Inferior_Trasera', models.CharField(max_length=100)),
                ('Altura_Calza_Inferior_Izquierda', models.CharField(max_length=100)),
                ('Altura_Calza_Inferior_Derecha', models.CharField(max_length=100)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monttools.datos_principales')),
            ],
        ),
    ]
