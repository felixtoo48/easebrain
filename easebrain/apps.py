from django.apps import AppConfig


class EasebrainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'easebrain'

    def ready(self):
        # Import signals
        import easebrain.signals
