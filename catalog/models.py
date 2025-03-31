from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField()
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="cook_set",  # Unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="cook_permissions_set",  # Unique related name
        blank=True
    )

    def __str__(self):
        return self.username


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook)
