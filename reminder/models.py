from django.db import models
from datetime import datetime

class Reminder(models.Model):
    email = models.EmailField(verbose_name='')
    text = models.TextField(verbose_name='Text', max_length=400)
    delay = models.IntegerField(verbose_name='Delay', default=10)
    duetime = models.DateTimeField(verbose_name='Due time', default=datetime.now, blank=True)

    def __str__(self):
        return f'Return to {self.email} if overdue more than {self.delay} minutes'

