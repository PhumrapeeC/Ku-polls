from django.apps import AppConfig


class PollsConfig(AppConfig):
    """
    AppConfig for the 'polls' app.

    This AppConfig is responsible for configuring the 'polls' app within the Django project.

    Attributes:
        default_auto_field (str): The name of the default AutoField to use for models.
        name (str): The name of the app, which is 'polls'.
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
