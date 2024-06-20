from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *
from .utils import get_one_template, get_template, post_template, put_template, delete_template


# ORDER API
@api_view(['GET'])
def get_order_api(request, order_id=None):
    serializer = OrderSerializer
    if order_id is not None:
        data = get_one_template(request, Order, serializer, order_id)
        return Response({"data": data}, status=status.HTTP_200_OK)
    else:
        data = get_template(request, Order, serializer)
        return Response({"data": data}, status=status.HTTP_200_OK)

@swagger_auto_schema(request_body=OrderSerializer, method='POST')
@api_view(['POST'])
def add_order_api(request):
    data, HttpStatus = post_template(request, OrderSerializer)
    return Response(data, status=HttpStatus)

@swagger_auto_schema(request_body=OrderSerializer, method='PUT')
@api_view(['PUT'])
def update_order_api(request, order_id):
    data, HttpStatus = put_template(request, Order, OrderSerializer, order_id)
    return Response(data, status=HttpStatus)

@api_view(['DELETE'])
def delete_order_api(request, order_id):
    data, HttpStatus = delete_template(request, Order, order_id)
    return Response(data, status=HttpStatus)


# ORDER PRODUCT API
@api_view(['GET'])
def get_order_product_api(request, order_id=None):
    serializer = OrderProductSerializer
    if order_id is not None:
        data = get_one_template(request, OrderProduct, serializer, order_id)
        return Response({"data": data}, status=status.HTTP_200_OK)
    else:
        data = get_template(request, OrderProduct, serializer)
        return Response({"data": data}, status=status.HTTP_200_OK)

@swagger_auto_schema(request_body=OrderProductSerializer, method='POST')
@api_view(['POST'])
def add_order_product_api(request):
    data, HttpStatus = post_template(request, OrderProductSerializer)
    return Response(data, status=HttpStatus)

@swagger_auto_schema(request_body=OrderProductSerializer, method='PUT')
@api_view(['PUT'])
def update_order_product_api(request, order_id):
    data, HttpStatus = put_template(request, OrderProduct, OrderProductSerializer, order_id)
    return Response(data, status=HttpStatus)

@api_view(['DELETE'])
def delete_order_product_api(request, order_id):
    data, HttpStatus = delete_template(request, OrderProduct, order_id)
    return Response(data, status=HttpStatus)
