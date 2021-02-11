from django.db import models

# Create your models here.

class Contato(models.Model):
        SUGESTAO = 'SG'
        CRITICAS = 'CT'
        DIVERSOS = 'DV'

        ASSUNTO = [
                (SUGESTAO, 'Sugestões'),
                (CRITICAS, 'Críticas'),
                (DIVERSOS, 'Diverso'),
        ]


        nome = models.CharField(max_length=40, blank=True, null=False)
        email =  models.EmailField(blank=True, null=False)
        assunto = models.CharField(max_length=2, choices=ASSUNTO, default=SUGESTAO)
        descricao = models.TextField(max_length=240, blank=False, null=False)

        def __str__(self):
                if self.email == '': self.email = 'Anonimo'
                return f'{self.email} - Assunto: {self.assunto}'