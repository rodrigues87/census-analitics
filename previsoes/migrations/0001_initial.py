# Generated by Django 3.0.8 on 2021-08-19 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('census', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Previsao',
            fields=[
                ('census_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='census.Census')),
                ('acertou', models.BooleanField(default=False)),
            ],
            bases=('census.census',),
        ),
    ]
