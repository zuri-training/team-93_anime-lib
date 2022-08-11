
from django.db import models

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length= 50, blank= True, default= "No name")
    body = models.TextField()
    role = models.CharField(max_length= 200, blank= True, default= "No role")
    
    # for  ordering 
    created = models.DateTimeField(auto_now_add= True)
     
    """ 
    so you see newer comments first, which might actually be more 
    relevant from a designers ux point of view
    to anybody
    """
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.body