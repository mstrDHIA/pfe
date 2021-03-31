import json
from datetime import datetime, timezone

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Buyer, Order, FeedBack, Block, Seller_Type, Seller, Payement_Methods, Profile, Order_Items
from .serializers import BuyerSerializer, OrderSerializer, FeedBackSerializer, BlockSerializer, SellerTypeSerializer, SellerSerializer, PayementMethodSerializer, ProfileSerializer, OrderItemSerializer, UserSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
def buyer_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        buyer = Buyer.objects.all()
        serializer = BuyerSerializer(buyer, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BuyerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def buyer_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        buyer = Buyer.objects.get(pk=pk)
    except Buyer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BuyerSerializer(buyer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BuyerSerializer(buyer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        buyer.delete()
        return HttpResponse(status=204)

@csrf_exempt
def order_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def order_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        order.delete()
        return HttpResponse(status=204)

@csrf_exempt
def feedback_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        feedback = FeedBack.objects.all()
        serializer = BuyerSerializer(feedback, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeedBackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def feedback_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        feedback = FeedBack.objects.get(pk=pk)
    except FeedBack.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FeedBackSerializer(feedback)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FeedBackSerializer(feedback, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        feedback.delete()
        return HttpResponse(status=204)

@csrf_exempt
def block_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        block = Block.objects.all()
        serializer = BlockSerializer(block, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def block_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        block = Block.objects.get(pk=pk)
    except Block.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlockSerializer(block)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BlockSerializer(block, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        block.delete()
        return HttpResponse(status=204)

@csrf_exempt
def sellertype_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        sellertype = Seller_Type.objects.all()
        serializer = SellerTypeSerializer(sellertype, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SellerTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def sellertype_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        sellertype = Seller_Type.objects.get(pk=pk)
    except Seller_Type.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SellerTypeSerializer(sellertype)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SellerTypeSerializer(sellertype, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sellertype.delete()
        return HttpResponse(status=204)

@csrf_exempt
def seller_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        seller = Seller.objects.all()
        serializer = SellerSerializer(seller, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SellerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def seller_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        seller = Seller.objects.get(pk=pk)
    except Seller.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer =   SellerSerializer(seller)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SellerSerializer(seller, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        seller.delete()
        return HttpResponse(status=204)

@csrf_exempt
def payement_methods_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        payement_methods = Payement_Methods.objects.all()
        serializer = PayementMethodSerializer(payement_methods, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PayementMethodSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def payement_methods_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        payement_methods = Payement_Methods.objects.get(pk=pk)
    except Payement_Methods.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PayementMethodSerializer(payement_methods)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PayementMethodSerializer(payement_methods, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        payement_methods.delete()
        return HttpResponse(status=204)
@csrf_exempt
def profile_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def profile_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        profile.delete()
        return HttpResponse(status=204)

@csrf_exempt
def order_items_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        order_items = Order_Items.objects.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrderItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def order_items_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        order_items = Order_Items.objects.get(pk=pk)
    except Order_Items.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrderItemSerializer(order_items)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderItemSerializer(order_items, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        order_items.delete()
        return HttpResponse(status=204)

@csrf_exempt
def available_orders(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        order = Order.objects.all()

        resultserializertab=[]
        for i in range(0,len(order),1):
            if(order[i].state=="pending"):
                intermediateresult=[]
                orderserializer = OrderSerializer(order[i], many=False)
                o=orderserializer.data
                intermediateresult.append(o)


                buyer = Buyer.objects.filter(id=order[i].id_buyer_id)
                buyerserializer = BuyerSerializer(buyer[0], many=False)
                b=buyerserializer.data
                intermediateresult.append(b)

                seller = Seller.objects.filter(id=order[i].id_seller_id)
                sellerserializer = SellerSerializer(seller[0], many=False)
                s=sellerserializer.data
                intermediateresult.append(s)
                payement_methods = Payement_Methods.objects.filter(id=order[i].id_payement_id)
                payementserializer = PayementMethodSerializer(payement_methods[0], many=False)
                p = payementserializer.data

                intermediateresult.append(p)

                orderitems = Order_Items.objects.all().filter()
                print(orderitems)
                items=[]
                print(order[i].id)
                for j in range(0, len(orderitems), 1):
                    print(orderitems[j].id_order_id)
                    print(orderitems[j].id_order_id==order[i].id)
                    if(orderitems[j].id_order_id==order[i].id):
                        print("l9itha")
                        orderitemserializer = OrderItemSerializer(orderitems[j], many=False)
                        oi = orderitemserializer.data
                        items.append(oi)
                intermediateresult.append(items)

                resultserializertab.append(intermediateresult)
        return JsonResponse(resultserializertab, safe=False)

@csrf_exempt
def user_info(request,pk):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        info=[]
        user = get_user_model().objects.filter(id=pk)
        userserializer = UserSerializer(user, many=True)
        profile = Profile.objects.filter(id=pk)
        profileserializer = ProfileSerializer(profile, many=True)
        info.append(userserializer.data)
        info.append(profileserializer.data)
        return JsonResponse(info, safe=False)


@csrf_exempt
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        user = get_user_model().objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = get_user_model().objects.get(pk=pk)
    except get_user_model().DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)


@csrf_exempt
def accept_order(request,pk):
    """
    List all code snippets, or create a new snippet.
    """

    try:
        order = Order.objects.get(pk=pk)
    except Order().DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'PUT':

        data = JSONParser().parse(request)
        print(data)
        serializer = OrderSerializer(order, data=data)

        #serializer.data
        if serializer.is_valid():
            serializer.validated_data["state"] = "delivering"
            print(serializer.validated_data["state"])
            serializer.validated_data["accept_time"] = datetime.now(timezone.utc)

            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def confirm_order(request,pk):
    """
    List all code snippets, or create a new snippet.
    """

    try:
        order = Order.objects.get(pk=pk)
    except Order().DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'PUT':

        data = JSONParser().parse(request)
        print(data)
        serializer = OrderSerializer(order, data=data)

        #serializer.data
        if serializer.is_valid():
            serializer.validated_data["state"] = "delivered"
            print(serializer.validated_data["state"])
            #now.strftime("%d/%m/%Y %H:%M:%S")
            serializer.validated_data["delivery_time"] = datetime.now(timezone.utc)
          #  serializer.validated_data["delivery_time"] = datetime.now()
            print(serializer.validated_data["delivery_time"]-serializer.validated_data["accept_time"])
            t=serializer.validated_data["accept_time"]-serializer.validated_data["delivery_time"]
            period=t.total_seconds()/60
            serializer.validated_data["delivery_durations"]=str(period)
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)




permission_classes = (IsAuthenticated,)
@csrf_exempt
def get(self, request):
    content = {'message': 'Hello, World!'}
    return Response(content)

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)




@csrf_exempt
def create_new_user(request):
    if request.method == 'POST':
        print(request)
        data = JSONParser().parse(request)
        print(data)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            x={
                "id_user":serializer.data["id"]
            }
            data=json.dumps(x)
            print(data)
            proser = ProfileSerializer(data=x)
            if proser.is_valid():
                proser.save()
                return JsonResponse(proser.data, status=201)
            print(proser.data)
            return JsonResponse(proser.errors, status=400)


           #return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
