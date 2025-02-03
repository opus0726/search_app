from django.db import models
 
class Items(models.Model): 
    id = models.CharField(max_length=255, primary_key=True)
    def __str__(self): 
        return self.id

class Review(models.Model):
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)