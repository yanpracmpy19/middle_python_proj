from django.contrib import admin
from .models import Genre
from .models import Filmwork
from .models import GenreFilmwork
from .models import Person
from .models import PersonFilmwork
#https://docs.djangoproject.com/en/3.1/ref/contrib/admin/


# для отображения с Кинопроизведениями
class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork
    raw_id_fields = ("person",) # иначе в select-box загружаются все persons


# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # Отображение полей в списке
    list_display = ('name', 'description', 'created', 'modified')
    # Фильтрация в списке
    list_filter = ('name', 'description',)
    # Поиск по полям
    search_fields = ('name', 'description',)


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    # для отображения с Кинопроизведениями
    #inlines = (GenreFilmworkInline,PersonFilmworkInline,)
    inlines = (GenreFilmworkInline,PersonFilmworkInline,)
    # Отображение полей в списке
    list_display = ('title', 'type', 'creation_date', 'rating', 'created', 'modified')
    # Фильтрация в списке
    list_filter = ('type',)
    # Поиск по полям
    search_fields = ('title', 'description', 'id')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # Отображение полей в списке
    list_display = ('id', 'full_name', 'modified',)
    # Поиск по полям
    search_fields = ('id', 'full_name',) # иначе в select-box загружаются все persons
    # чтобы было легче искать в popup

