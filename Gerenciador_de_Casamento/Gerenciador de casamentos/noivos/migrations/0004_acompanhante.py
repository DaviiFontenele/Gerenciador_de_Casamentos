# Generated by Django 5.1.2 on 2024-11-02 23:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noivos', '0003_presentes_reservado_por'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanhante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('convidado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acompanhantes', to='noivos.convidados')),
            ],
        ),
    ]
