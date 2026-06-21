from django.db import models

# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.BigIntegerField()
    district = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)
    dob = models.DateField()
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)


class Complaint(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    complaint = models.CharField(max_length=500)
    reply = models.CharField(max_length=500)
    status = models.CharField(max_length=100)


class Review(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    review = models.CharField(max_length=500)
    rating = models.CharField(max_length=200)


class Feedback(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    feedback = models.CharField(max_length=500)


class Upload(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    file = models.CharField(max_length=500)
    title = models.CharField(max_length=500)







