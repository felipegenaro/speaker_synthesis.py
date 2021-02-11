from django.shortcuts import render

# Create your views here.

def tts_index(request):
        return render(request, 'text_to_speech.html')