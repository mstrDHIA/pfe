from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.


class Buyer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    long=models.CharField(default="unknown",max_length=200)
    lat=models.CharField(default="unknown",max_length=200)
    email=models.CharField(max_length=30)

class FeedBack(models.Model):
    USER = get_user_model()
    id_user = models.ForeignKey(USER, on_delete=models.SET('unknown'))
    date = models.DateTimeField(default=datetime.now)
    object = models.CharField(max_length=30)
    message = models.CharField(max_length=2000)

class Block(models.Model):
    USER = get_user_model()
    id_user = models.ForeignKey(USER, on_delete=models.SET('unknown'))
    id_buyer = models.ForeignKey(Buyer, on_delete=models.SET('unknown'))
    date = models.DateTimeField(default=datetime.now)
    blocker = models.CharField(max_length=20)
    reason = models.CharField(max_length=100)
class Seller_Type(models.Model):
    name = models.CharField(max_length=10)

class Seller (models.Model):
    name = models.CharField(max_length=20)
    id_sellertype = models.ForeignKey(Seller_Type, on_delete=models.SET('unknown'))
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    long = models.CharField(default="unknown", max_length=200)
    lat = models.CharField(default="unknown", max_length=200)

class Payement_Methods(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

class Order(models.Model):
    USER = get_user_model()
    id_user = models.ForeignKey(USER, null=True, on_delete=models.SET('unknown'), )
    id_buyer = models.ForeignKey(Buyer, on_delete=models.SET('unknown'))
    id_payement = models.ForeignKey(Payement_Methods, on_delete=models.SET('unknown'))
    id_seller = models.ForeignKey(Seller, on_delete=models.SET('unknown'))
    buyer_phone = models.CharField(max_length=20)
    buyer_mail = models.CharField(max_length=30)
    total_price = models.FloatField(default=0)
    delivery_fees = models.FloatField(default=0)
    price = models.FloatField(default=0)
    stars = models.IntegerField(blank=True, null=True)
    review = models.CharField(max_length=200, null=True)
    delivery_time = models.DateTimeField(null=True, )
    delivery_durations = models.FloatField(null=True, )
    accept_time=models.DateTimeField(null=True)
    
    order_time = models.DateTimeField()
    
    order_type = models.CharField(max_length=20)
    is_paid = models.BooleanField()
    distance = models.FloatField()
    order_duration = models.FloatField()

    state = models.CharField(default="pending", max_length=10)


class Order_Items(models.Model):
    id_order = models.ForeignKey(Order, on_delete=models.SET('unknown'))
    name = models.CharField(max_length=20)
    price = models.FloatField()
    count = models.IntegerField()


class Profile(models.Model):
    USER = get_user_model()
    id_user = models.ForeignKey(USER, on_delete=models.SET('unknown'),unique=True)
    age = models.IntegerField(default=0,null=True)
    sex = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=50,null=True)

    country = models.CharField(max_length=20,null=True)
    governorate = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=20,null=True)
    state = models.CharField(max_length=10,null=True)
    lat = models.CharField(max_length=20,null=True)
    long = models.CharField(max_length=20,null=True)
    photo = models.ImageField(null=True)
    #Image = models.FileField(null=True)
    vehicle = models.CharField(max_length=15,null=True)

    phone=models.IntegerField(max_length=12,null=True)







