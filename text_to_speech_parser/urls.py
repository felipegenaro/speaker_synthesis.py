"""text_to_speech_parser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from landing.views import render_index
from contato.views import adicionar_contato
from text_to_speech.views import tts_index
from speech_to_text.views import stt_index
from file_to_speech.views import fts_index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_index, name='home'),
    path('contato/', adicionar_contato, name='contato'),
    path('text_to_speech/', tts_index, name='text_to_speech'),
    path('speech_to_text/', stt_index, name='speech_to_text'),
    path('file_to_speech/', fts_index, name='file_to_speech'),

]
