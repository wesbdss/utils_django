import os, sys

# Importar APlicação Django para outros projetos fora do projeto atual
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myjobszone.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
