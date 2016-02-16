"""
WSGI config for baseball_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

proj_path = '/Users/zcalabrese/Google Drive/development/a_baseball_project'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baseball_project.settings")

os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


"""
from django.core.wsgi import get_wsgi_application

#os.environ['DJANGO_SETTINGS_MODULE'] = "baseball_project.settings"

application = get_wsgi_application()
"""
