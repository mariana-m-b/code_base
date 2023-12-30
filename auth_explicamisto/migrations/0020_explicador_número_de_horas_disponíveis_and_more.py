# Generated by Django 5.0 on 2023-12-27 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_explicamisto', '0019_alter_user_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='explicador',
            name='número_de_horas_disponíveis',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
