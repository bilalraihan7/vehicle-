from django.db import models
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)

class booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    fare = models.FloatField()
    rating = models.FloatField(null=True, blank=True)


class vehicle(models.Model):
    vehicle_name = models.CharField(max_length=100)
    vehicle_reg= models.IntegerField()
    vehicle_type= models.CharField(max_length=500)
    vehicle_image =models.ImageField(upload_to="",blank=True)
    

