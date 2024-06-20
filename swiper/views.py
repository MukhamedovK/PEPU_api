from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *
from .utils import get_one_template, get_template, post_template, put_template, delete_template

# SHOWCASE SWIPER API
@api_view(['GET'])
def get_showcase_swiper_api(request, obj_id=None):
    serializer = ShowcaseSwiperSerializer
    if obj_id is not None:
        data = get_one_template(request, ShowcaseSwiper, serializer, obj_id)
        return Response({"data": data}, status=status.HTTP_200_OK)
    else:
        data = get_template(request, ShowcaseSwiper, serializer)
        return Response({"data": data}, status=status.HTTP_200_OK)
    
@swagger_auto_schema(request_body=ShowcaseSwiperSerializer, method='POST')
@api_view(['POST'])
def add_showcase_swiper_api(request):
    data, HttpStatus = post_template(request, ShowcaseSwiperSerializer)
    return Response(data, status=HttpStatus)

@swagger_auto_schema(request_body=ShowcaseSwiperSerializer, method='PUT')
@api_view(['PUT'])
def update_showcase_swiper_api(request, obj_id):
    data, HttpStatus = put_template(request, ShowcaseSwiper, ShowcaseSwiperSerializer, obj_id)
    return Response(data, status=HttpStatus)

@api_view(['DELETE'])
def delete_showcase_swiper_api(request, obj_id):
    data, HttpStatus = delete_template(request, ShowcaseSwiper, obj_id)
    return Response(data, HttpStatus)
    

# SHOWCASE SUB SWIPER API
@api_view(['GET'])
def get_showcase_sub_swiper_api(request, obj_id=None):
    serializer = ShowcaseSubSwiper
    if obj_id is not None:
        data = get_one_template(request, ShowcaseSubSwiper, serializer, obj_id)
        return Response({"data": data}, status=status.HTTP_200_OK)
    else:
        data = get_template(request, ShowcaseSubSwiper, serializer)
        return Response({"data": data}, status=status.HTTP_200_OK)

@swagger_auto_schema(request_body=ShowcaseSubSwiperSerializer, method='POST')
@api_view(['POST'])
def add_showcase_sub_swiper_api(request):
    data, HttpStatus = post_template(request, ShowcaseSubSwiperSerializer)
    return Response(data, status=HttpStatus)

@swagger_auto_schema(request_body=ShowcaseSubSwiperSerializer, method='PUT')
@api_view(['PUT'])
def update_showcase_sub_swiper_api(request, obj_id):
    data, HttpStatus = put_template(request, ShowcaseSubSwiper, ShowcaseSubSwiperSerializer, obj_id)
    return Response(data, status=HttpStatus)

@api_view(['DELETE'])
def delete_showcase_sub_swiper_api(request, obj_id):
    data, HttpStatus = delete_template(request, ShowcaseSubSwiper, obj_id)
    return Response(data, HttpStatus)
    

# CLOTHES SWIPER API
@api_view(['GET'])
def get_clothes_swiper_api(request, obj_id=None):
    serializer = ClothesSwiperSerializer
    if obj_id is not None:
        data = get_one_template(request, ClothesSwiper, serializer, obj_id)
        return Response({"data": data}, status=status.HTTP_200_OK)
    else:
        data = get_template(request, ClothesSwiper, serializer)
        return Response({"data": data}, status=status.HTTP_200_OK)
    
@swagger_auto_schema(request_body=ClothesSwiperSerializer, method='POST')
@api_view(['POST'])
def add_clothes_swiper_api(request):
    data, HttpStatus = post_template(request, ClothesSwiperSerializer)
    return Response(data, status=HttpStatus)

@swagger_auto_schema(request_body=ClothesSwiperSerializer, method='PUT')
@api_view(['PUT'])
def update_clothes_swiper_api(request, obj_id):
    data, HttpStatus = put_template(request, ClothesSwiper, ClothesSwiperSerializer, obj_id)
    return Response(data, status=HttpStatus)

@api_view(['DELETE'])
def delete_clothes_swiper_api(request, obj_id):
    data, HttpStatus = delete_template(request, ClothesSwiper, obj_id)
    return Response(data, HttpStatus)
