from django.db import models

class Record(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    message = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', default = 1, on_delete=models.CASCADE, to_field = 'username') 

    class Meta:
        ordering = ['created']
