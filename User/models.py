from django.db import models

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    username=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Post(models.Model):
    user=models.ForeignKey(User,max_length=100,on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.CharField(max_length=100)
    updated_at=models.CharField(max_length=100)

    

