# Generated by Django 2.2.7 on 2020-10-20 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteForum', '0004_auto_20201019_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resp', models.TextField()),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteForum.enquete')),
            ],
            options={
                'verbose_name': 'Resposta',
                'verbose_name_plural': 'Respostas',
            },
        ),
    ]
