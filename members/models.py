from django.db import models

# Create your models here.
class Member(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.title
        #hoặc return f'{self.firstname} {self.lastname}
    
    
    

    