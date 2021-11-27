# Generated by Django 3.2.9 on 2021-11-14 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(null=True, verbose_name='Рейтинг фильма'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='genres.genre', verbose_name='Жанр'),
        ),
    ]
