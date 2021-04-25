#from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Buyer, Order, FeedBack, Block, Seller_Type, Seller, Payement_Methods, Profile, Order_Items
from django.contrib.auth.models import User


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Buyer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.long = validated_data.get('long', instance.long)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance


class RegisterUserSerializer(serializers.ModelSerializer):


    class Meta:

        model = User

        exclude = ('groups', 'user_permissions')
        extra_kwargs = {'password': {'write_only': True}}

#       model = get_user_model()
        #exclude = ('groups', 'user_permissions')
      #  exclude = ['password']
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user




class UserSerializer(serializers.ModelSerializer):


    class Meta:

 #       model = get_user_model()
        model = User
        exclude = ('groups', 'user_permissions')
        extra_kwargs = {'password': {'write_only': True}}

#  exclude = ['password']
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """

        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.password = validated_data.get('password', instance.password)
        instance.last_login = validated_data.get('last_login', instance.last_login)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.save()
        return instance

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id_buyer = validated_data.get('id_buyer', instance.id_buyer)
        instance.id_seller = validated_data.get('id_seller', instance.id_seller)
        instance.id_user = validated_data.get('id_user', instance.id_user)
        instance.buyer_phone = validated_data.get('buyer_phone', instance.buyer_phone)
        instance.id_payement = validated_data.get('id_payement', instance.id_payement)
        instance.is_paid = validated_data.get('is_paid', instance.is_paid)
        instance.price = validated_data.get('price', instance.price)
        instance.order_duration = validated_data.get('order_duration', instance.order_duration)
        instance.order_time = validated_data.get('order_time', instance.order_time)
        instance.delivery_time = validated_data.get('delivery_time', instance.delivery_time)
        instance.accept_time = validated_data.get('accept_time', instance.accept_time)
        instance.delivery_durations = validated_data.get('delivery_durations', instance.delivery_durations)
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.delivery_fees = validated_data.get('delivery_fees', instance.delivery_fees)
        instance.buyer_mail = validated_data.get('buyer_mail', instance.buyer_mail)
        instance.state = validated_data.get('state', instance.state)
        instance.stars = validated_data.get('stars', instance.stars)
        instance.review = validated_data.get('review', instance.review)
        instance.distance = validated_data.get('distance', instance.distance)
        instance.order_type = validated_data.get('order_type', instance.order_type)
        instance.save()
        return instance

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return FeedBack.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id_order = validated_data.get('id_order', instance.id_order)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.count = validated_data.get('count', instance.count)

        instance.save()
        return instance

class BlockSerializer(serializers.ModelSerializer):


    class Meta:
        model = Block
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Block.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id_user = validated_data.get('id_user', instance.id_user)
        instance.id_buyer = validated_data.get('id_buyer', instance.id_buyer)
        instance.date = validated_data.get('date', instance.date)
        instance.blocker = validated_data.get('blocker', instance.blocker)
        instance.reason = validated_data.get('reason', instance.reason)
        instance.save()
        return instance

class SellerTypeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Seller_Type
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Seller_Type.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class SellerSerializer(serializers.ModelSerializer):


    class Meta:
        model = Seller
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Seller.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.id_sellertype = validated_data.get('id_sellertype', instance.id_sellertype)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('name', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.long = validated_data.get('long', instance.long)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.save()
        return instance

class PayementMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payement_Methods
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Payement_Methods.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)


        return instance

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id_user = validated_data.get('id_user', instance.id_user)
        instance.age = validated_data.get('age', instance.age)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.address = validated_data.get('address', instance.address)

        instance.country = validated_data.get('country', instance.country)
        instance.governorate = validated_data.get('governorate', instance.governorate)
        instance.city = validated_data.get('city', instance.city)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.long = validated_data.get('long', instance.long)
        instance.vehicle = validated_data.get('vehicle', instance.vehicle)
        instance.state = validated_data.get('state', instance.state)
        instance.photo = validated_data.get('photo', instance.photo)
        #instance.image = validated_data.get('image', instance.image)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.delivered_orders = validated_data.get('delivered_orders', instance.delivered_orders)
        instance.failed_orders = validated_data.get('failed_orders', instance.failed_orders)
        instance.stars = validated_data.get('stars', instance.stars)
        instance.profits = validated_data.get('profits', instance.profits)


        return instance

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Items
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Order_Items.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id_order = validated_data.get('id_order', instance.id_order)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.count = validated_data.get('count', instance.count)

        return instance


