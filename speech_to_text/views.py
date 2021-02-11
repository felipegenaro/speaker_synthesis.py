from django.shortcuts import render

# Create your views here.

def stt_index(request):
        return render(request, 'speech_to_text.html')