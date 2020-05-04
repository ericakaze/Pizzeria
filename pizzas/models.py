from django.db import models

class Pizza(models.Model):
    name= models.CharField(max_length=200)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

 
class topping (models.Model):
    pizza=models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    date_added= models.DateTimeField(auto_now_add=True)

    """ class Meta:
        verbose_name_plural ='entries' """
    
    def __str__(self):
        return f"{self.name[:50]} ..."

class new_comment (models.Model):
    pizza=models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text=models.TextField()
    """ class Meta:
        verbose_name_plural ='entries' """
    
    def __str__(self):
        return f"{self.name[:50]} ..."

