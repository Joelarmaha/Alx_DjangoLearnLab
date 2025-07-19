from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'
    
class RelationshipAppConfig(AppConfig):  # or your actual app name
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'  # replace with your app name

    def ready(self):
        import relationship_app.signals  # replace with your app name