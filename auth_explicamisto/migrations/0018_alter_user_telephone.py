# Generated by Django 5.0 on 2023-12-27 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_explicamisto', '0017_alter_aluno_distrito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.IntegerField(max_length=9),
        ),
    ]
