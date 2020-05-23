from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

class Car(models.Model):
    customer = models.ForeignKey(Customer, related_name='cars', on_delete=models.CASCADE)
    year = models.IntegerField()
    model = models.CharField(max_length=50)
    vin = models.CharField(max_length=50)

    def __str__(self):
        return self.model


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
