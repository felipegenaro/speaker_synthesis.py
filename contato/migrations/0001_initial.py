# Generated by Django 3.1.6 on 2021-02-11 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('assunto', models.CharField(choices=[('SG', 'Sugestões'), ('CT', 'Críticas'), ('DV', 'Diverso')], default='SG', max_length=2)),
                ('descricao', models.TextField(max_length=240)),
            ],
        ),
    ]
