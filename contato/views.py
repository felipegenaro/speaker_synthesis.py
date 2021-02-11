from django.shortcuts import render
from contato.forms import ContatoCriarForm

# Create your views here.

def adicionar_contato(request):
        formulario = ContatoCriarForm(request.POST or None)

        if formulario.is_valid():
                # formulario.fields['nome']
                if formulario.fields['nome'] == '': formulario.fields['nome'] = 'Anonimo'
                if formulario.fields['email'] == '': formulario.fields['email'] = 'Anonimo'
                formulario.save()
                formulario = ContatoCriarForm()

        context = {
                'form': formulario
        }
        
        return render(request, 'contato.html', context)