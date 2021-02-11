from django.shortcuts import render

# Create your views here.

def fts_index(request):
        return render(request, 'file_to_speech.html')