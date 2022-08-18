from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies' # тут делать нельзя lazy gettext
    #verbose_name = 'Стрим им.М.А.Булгакова'
    verbose_name = _('BULGAKOVSTREAM')
