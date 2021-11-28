from django.contrib import admin
from genres.models import Genre


class GenreAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name',)


admin.site.register(Genre, GenreAdmin)

