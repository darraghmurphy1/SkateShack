from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Skateboard(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='skateboard_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SkateboardDeck(models.Model):
    skateboard = models.ForeignKey(Skateboard, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    width = models.FloatField()
    length = models.FloatField()
    image = models.ImageField(upload_to='deck_images/')

    def __str__(self):
        return f"{self.skateboard} - Deck"

class SkateboardTruck(models.Model):
    skateboard = models.ForeignKey(Skateboard, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    width = models.FloatField()
    image = models.ImageField(upload_to='truck_images/')

    def __str__(self):
        return f"{self.skateboard} - Truck"

class SkateboardWheels(models.Model):
    skateboard = models.ForeignKey(Skateboard, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    width = models.FloatField()
    image = models.ImageField(upload_to='wheels_images/')

    def __str__(self):
        return f"{self.skateboard} - Wheels"

class SkateboardHardware(models.Model):
    skateboard = models.ForeignKey(Skateboard, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hardware_images/')

    def __str__(self):
        return self.brand + ' ' + self.type + ' ' + self.size + ' ' + self.color
