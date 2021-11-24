from django.db import models

class User(models.Model):
    email      = models.EmailField()
    password   = models.CharField(max_length=200)
    name       = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
    




