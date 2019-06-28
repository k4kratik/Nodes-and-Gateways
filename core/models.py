from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Block(models.Model):
    block_name = models.CharField(max_length=31)

    def __str__(self):
        return self.block_name


class Gateway(models.Model):
    gateway_name = models.CharField(unique=True, max_length=31)
    x_coordinate = models.DecimalField(max_digits=9, decimal_places=6,
                                       validators=[MaxValueValidator(180), MinValueValidator(-180)])  # Longitude
    y_coordinate = models.DecimalField(max_digits=9, decimal_places=6,
                                       validators=[MaxValueValidator(90), MinValueValidator(-90)])  # Latitude
    number_nodes = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.gateway_name


class Node(models.Model):
    node_name = models.CharField(unique=True, max_length=31)
    gateway_id = models.ForeignKey(Gateway, on_delete=models.CASCADE)
    x_coordinate = models.DecimalField(max_digits=9, decimal_places=6,
                                       validators=[MaxValueValidator(180), MinValueValidator(-180)])  # Longitude
    y_coordinate = models.DecimalField(max_digits=9, decimal_places=6,
                                       validators=[MaxValueValidator(90), MinValueValidator(-90)])  # Latitude
    block_id = models.ForeignKey(Block, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.node_name 