from django.apps import AppConfig


class Practice13Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'practice13'

    def ready(self) -> None:
        import practice13.signals
