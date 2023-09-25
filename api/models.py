from django.db import models

class datacon(models.Model):
    title = models.TextField(blank=True,null = False)
    subtitle = models.TextField(blank=True,null = False)
    content = models.TextField(blank=True,null = False)
    
    def __str__(self):
        return self.title
