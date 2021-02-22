from django.db import models

# Create your models here.

class Contact(models.Model):
        SUGESTION = 'SG'
        CRITICISM = 'CT'
        DIVERSE = 'DV'

        SUBJECT = [
                (SUGESTION, 'Sugestion'),
                (CRITICISM, 'Criticism'),
                (DIVERSE, 'Diverse'),
        ]


        name = models.CharField(max_length=40, blank=True, null=False)
        email =  models.EmailField(blank=True, null=False)
        subject = models.CharField(max_length=2, choices=SUBJECT, default=SUGESTION)
        description = models.TextField(max_length=240, blank=False, null=False)

        def __str__(self):
                if self.email == '': self.email = 'Anonymous'
                return f'{self.email} - Subject: {self.subject}'