import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings #чтобы иметь возможность смотреть на переенные из .env->settings.py

# python manage.py inspectdb
# команда может построить файл на основе схемы БД


# part for Mixin-Classes
class TimeStampedMixin(models.Model):
    # auto_now_add автоматически выставит дату создания записи
    created = models.DateTimeField(_('created_ts1'), auto_now_add=True)
    # auto_now изменятся при каждом обновлении записи
    modified = models.DateTimeField(_('modified'),auto_now=True)

    class Meta:
        # Этот параметр указывает Django, что этот класс не является представлением таблицы
        abstract = True


class UUIDMixin(models.Model):
    # Типичная модель в Django использует число в качестве id. В таких ситуациях поле не описывается в модели.
    # Вам же придётся явно объявить primary key.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


# Create your models here.
class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_('name'), max_length=255)
    # blank=True делает поле необязательным для заполнения.
    description = models.TextField(_('description'), blank=True)

    class Meta:
        # Ваши таблицы находятся в нестандартной схеме. Это нужно указать в классе модели
        db_table = "content\".\"genre"
        # Следующие два поля отвечают за название модели в интерфейсе
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

    def __str__(self):
        return self.name


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_('full_name'), max_length=255)

    class Meta:
        # Ваши таблицы находятся в нестандартной схеме. Это нужно указать в классе модели
        db_table = "content\".\"person"
        # Следующие два поля отвечают за название модели в интерфейсе
        verbose_name = _('Movieperson')
        verbose_name_plural = _('Moviepersons')

    def __str__(self):
        return self.full_name


class Filmwork(UUIDMixin, TimeStampedMixin):

    class FilmWorkTypesChoises(models.TextChoices):
        MOVIE_TYPE_CHOICE = 'movie', _('movie')
        TV_SHOW_TYPE_CHOICE  = 'tv_show', _('tv_show')

    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types
    title = models.CharField(_('title'), max_length=255)
    # blank=True делает поле необязательным для заполнения.
    description = models.TextField(_('description'), blank=True)
    creation_date = models.DateField(_('creation_date'), auto_now_add=True)
    # https: // docs.djangoproject.com / en / 3.2 / ref / validators /
    # поле с валидатором
    rating = models.FloatField(_('rating'), blank=True, default=1,
                                help_text=_('от1до100'),
                                validators=[MinValueValidator(0),MaxValueValidator(100)])
    type = models.CharField(
        max_length=10,
        choices=FilmWorkTypesChoises.choices,
        default=FilmWorkTypesChoises.MOVIE_TYPE_CHOICE,
    )
    certificate = models.CharField(_('certificate'), max_length=512, blank=True)
    # Параметр upload_to указывает, в какой подпапке будут храниться загружемые файлы.
    # Базовая папка указана в файле настроек как MEDIA_ROOT
    file_path = models.FileField(_('file'), blank=True, null=True, upload_to=settings.MEDIA_ROOT)

    # связи между таблицами/моделями/сущностями
    genres = models.ManyToManyField(Genre, through='GenreFilmwork')
    persons = models.ManyToManyField(Person, through='PersonFilmwork',)

    class Meta:
        # Ваши таблицы находятся в нестандартной схеме. Это нужно указать в классе модели
        db_table = "content\".\"film_work"
        # Следующие два поля отвечают за название модели в интерфейсе
        verbose_name = _('movie')
        verbose_name_plural = _('movies')

    def __str__(self):
        return self.title


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created = models.DateTimeField(_('created_genre'),auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"


class PersonFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.TextField('role', null=True)
    created = models.DateTimeField(_('created_personfilm'),auto_now_add=True)


    class Meta:
        db_table = "content\".\"person_film_work"
        unique_together = (('film_work', 'person'),)
