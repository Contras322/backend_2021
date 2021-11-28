from django.contrib import admin
from movies.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_filter = ('rating',)
    list_display = ('name',)


admin.site.register(Movie, MovieAdmin)
