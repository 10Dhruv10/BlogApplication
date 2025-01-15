"""
WSGI config for crashblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crashblog.settings')

application = get_wsgi_application()


#for virtual env->

# pip install virtualenv
# virtualenv ProjectName_env
#.\ProjectName_env\Scripts\activate

#if above one show error use this before .\blogapp_env line
#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
