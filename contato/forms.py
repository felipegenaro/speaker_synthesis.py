from django import forms
from contato.models import Contato

class ContatoCriarForm(forms.ModelForm):
        class Meta:
                model = Contato
                fields = [
                        'nome',
                        'email',
                        'assunto',
                        'descricao',
                ]