from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *
from .utils import get_one_template, get_template, post_template, put_template, delete_template


# PRODUCT API
@api_view(['GET'])
def get_product_api(request, product_id=None):
    serializer = ProductSerializer
    if product_id is not None:
        data = get_one_template(request, Product, serializer, product_id)
        return Response({"data": data}, status=status.HTTP_200_OK)
    else:
        data = get_template(request, Product, serializer)
        return Response({"data": data}, status=status.HTTP_200_OK)

@swagger_auto_schema(request_body=ProductSerializer, method='POST')
@api_view(['POST'])
def add_product_api(request):
    data, HttpStatus = post_template(request, ProductSerializer)
    return Response(data, status=HttpStatus)

@swagger_auto_schema(request_body=ProductSerializer, method='PUT')
@api_view(['PUT'])
def update_product_api(request, product_id):
    data, HttpStatus = put_template(request, Product, ProductSerializer, product_id)
    return Response(data, status=HttpStatus)

@api_view(['DELETE'])
def delete_product_api(request, product_id):
    data, HttpStatus = delete_template(request, Product, product_id)
    return Response(data, status=HttpStatus)


# CATEGORY API
@api_view(['GET'])
def get_category_api(request, category_id=None):
    serializer = CategorySerializer
    if category_id is not None:
        data = get_one_template(request, Category, serializer, category_id)
        return Response({"data": data}, status=status.HTTP_200_OK)
    else:
        data = get_template(request, Category, serializer)
        return Response({"data": data}, status=status.HTTP_200_OK)

@swagger_auto_schema(request_body=CategorySerializer, method='POST')
@api_view(['POST'])
def add_category_api(request):
    data, HttpStatus = post_template(request, CategorySerializer)
    return Response(data, status=HttpStatus)

@swagger_auto_schema(request_body=CategorySerializer, method='PUT')
@api_view(['PUT'])
def update_category_api(request, category_id):
    data, HttpStatus = put_template(request, Category, CategorySerializer, category_id)
    return Response(data, status=HttpStatus)

@api_view(['DELETE'])
def delete_category_api(request, category_id):
    data, HttpStatus = delete_template(request, Category, category_id)
    return Response(data, status=HttpStatus)


# SIZE API
@api_view(['GET'])
def get_size_api(request, size_id=None):
    serializer = SizeSerializer
    if size_id is not None:
        data = get_one_template(request, Size, serializer, size_id)
        return Response({"data": data}, status=status.HTTP_200_OK)
    else:
        data = get_template(request, Size, serializer)
        return Response({"data": data}, status=status.HTTP_200_OK)
    
@swagger_auto_schema(request_body=SizeSerializer, method='POST')
@api_view(['POST'])
def add_size_api(request):
    data, HttpStatus = post_template(request, SizeSerializer)
    return Response(data, status=HttpStatus)

@swagger_auto_schema(request_body=SizeSerializer, method='PUT')
@api_view(['PUT'])
def update_size_api(request, size_id):
    data, HttpStatus = put_template(request, Size, SizeSerializer, size_id)
    return Response(data, status=HttpStatus)

@api_view(['DELETE'])
def delete_size_api(request, size_id):
    data, HttpStatus = delete_template(request, Size, size_id)
    return Response(data, status=HttpStatus)


# PRODUCT PHOTO API
@api_view(['GET'])
def get_product_photo_api(request, product_photo_id=None):
    serializer = ProductPhotoSerializer
    if product_photo_id is not None:
        data = get_one_template(request, ProductPhoto, serializer, product_photo_id)
        return Response({"data": data}, status=status.HTTP_200_OK)
    else:
        data = get_template(request, ProductPhoto, serializer)
        return Response({"data": data}, status=status.HTTP_200_OK)
    
@swagger_auto_schema(request_body=ProductPhotoSerializer, method='POST')
@api_view(['POST'])
def add_product_photo_api(request):
    data, HttpStatus = post_template(request, ProductPhotoSerializer)
    return Response(data, status=HttpStatus)

@swagger_auto_schema(request_body=ProductPhotoSerializer, method='PUT')
@api_view(['PUT'])
def update_product_photo_api(request, product_photo_id):
    data, HttpStatus = put_template(request, ProductPhoto, ProductPhotoSerializer, product_photo_id)
    return Response(data, status=HttpStatus)

@api_view(['DELETE'])
def delete_product_photo_api(request, product_photo_id):
    data, HttpStatus = delete_template(request, ProductPhoto, product_photo_id)
    return Response(data, status=HttpStatus)

