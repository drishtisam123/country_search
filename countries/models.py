from django.db import models

class Country(models.Model):
    # Define a field to store the country name
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        # Return the country name when the object is printed
        return self.name
