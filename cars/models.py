from django.db import models

class Tire(models.Model):
    width        = models.PositiveIntegerField()
    aspect_ratio = models.PositiveIntegerField()
    wheel_size   = models.PositiveIntegerField()
    created_at   = models.DateTimeField(auto_now=True)
    updated_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tires'

class UserTire(models.Model):
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    tire       = models.ForeignKey('Tire', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_tires'
