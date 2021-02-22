from django.shortcuts import render
from contact.forms import ContactForm

# Create your views here.

def adicionar_contact(request):
        form = ContactForm(request.POST or None)

        if form.is_valid():
                # form.fields['name']
                if form.fields['name'] == '': form.fields['name'] = 'Anonymous'
                if form.fields['email'] == '': form.fields['email'] = 'Anonymous'
                form.save()
                form = ContactForm()

        context = {
                'form': form
        }
        
        return render(request, 'contact.html', context)