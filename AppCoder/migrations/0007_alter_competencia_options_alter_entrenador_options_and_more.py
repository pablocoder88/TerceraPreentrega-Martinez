# Generated by Django 5.0.6 on 2024-06-05 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_remove_entrenador_competencias_nadador_competencias'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competencia',
            options={'verbose_name': 'Competence', 'verbose_name_plural': 'Competences'},
        ),
        migrations.AlterModelOptions(
            name='entrenador',
            options={'verbose_name': 'Entrenador', 'verbose_name_plural': 'Entrenadores'},
        ),
        migrations.AlterModelOptions(
            name='nadador',
            options={'verbose_name': 'Nadador', 'verbose_name_plural': 'Nadadores'},
        ),
        migrations.AlterUniqueTogether(
            name='competencia',
            unique_together=set(),
        ),
    ]
