from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class House(models.Model):
    address = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='houses', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.address


class Rent(models.Model):
    user = models.ForeignKey(User, related_name='rents', on_delete=models.CASCADE)
    house = models.ForeignKey(House, related_name='rents', on_delete=models.CASCADE)  