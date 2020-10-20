# Generated by Django 2.2.7 on 2020-10-20 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='enquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'Enquete',
                'verbose_name_plural': 'Enquetes',
            },
        ),
    ]
