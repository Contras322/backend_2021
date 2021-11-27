# Generated by Django 3.2.9 on 2021-11-14 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=45, verbose_name='Название фильма')),
                ('genre_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='genres.genre', verbose_name='')),
            ],
        ),
    ]
