from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    portrait = models.ImageField(default='user_silhouette.png', null=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    ENGINE_LAYOUT_CHOICES = (
        ('Inline 4', 'Inline 4'),
        ('Inline 5', 'Inline 5'),
        ('Inline 6', 'Inline 6'),
        ('Flat 4', 'Flat 4'),
        ('Flat 6', 'Flat 6'),
        ('V6', 'V6'),
        ('V8', 'V8'),
    )
    FUEL_CHOICES = (
        ('Gasoline', 'Gasoline'),
        ('Diesel', 'Diesel'),
        ('Flex-Fuel', 'Flex-Fuel'),
    )
    customer = models.ForeignKey(Customer, related_name='cars', on_delete=models.CASCADE)
    year = models.IntegerField(blank=True)
    make = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50, blank=True)
    vin = models.CharField(max_length=50, blank=True)
    engine_size = models.CharField(max_length=50, blank=True)
    engine_layout = models.CharField(choices=ENGINE_LAYOUT_CHOICES, max_length=50, blank=True)
    fuel = models.CharField(choices=FUEL_CHOICES, max_length=50, blank=True)
    header_photo = models.ImageField(null=True)

    def __str__(self):
        return self.model


class CarFile(models.Model):
    file = models.FileField(null=False)
    car = models.ForeignKey(Car, related_name='files', on_delete=models.CASCADE)
    type = models.CharField(max_length=15)


class Comment(models.Model):
    car = models.ForeignKey(Car, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.content) >= 20:
            return f'{self.car.model} {self.content[:20]}...'
        else:
            return f'{self.car.model} {self.content}'
