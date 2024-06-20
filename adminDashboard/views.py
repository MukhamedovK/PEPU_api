from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serializers import ProfileSerializer, BranchSerializer
from .models import Profile, Branches
from .utils import get_one_template, get_template, post_template, put_template, delete_template, registration_check, login_check

# PROFILE API
@api_view(['GET'])
def get_profile_api(request, profile_id=None):
    serializer = ProfileSerializer
    if profile_id is not None:
        data = get_one_template(request, Profile, serializer, profile_id)
        return Response({"data": data}, status=status.HTTP_200_OK)
    else:
        data = get_template(request, Profile, serializer)
        return Response({"data": data}, status=status.HTTP_200_OK)
    
@swagger_auto_schema(request_body=ProfileSerializer, method='POST')
@api_view(['POST'])
def add_profile_api(request):
    error = registration_check(formData=request.data)
    if error is None:
        data, HttpStatus = post_template(request, ProfileSerializer)
        return Response(data, status=HttpStatus)
    return Response(error)

@swagger_auto_schema(request_body=ProfileSerializer, method='PUT')
@api_view(['PUT'])
def update_profile_api(request, profile_id):
    data, HttpStatus = put_template(request, Profile, ProfileSerializer, profile_id)
    return Response(data, status=HttpStatus)

@api_view(['DELETE'])
def delete_profile_api(request, profile_id):
    data, HttpStatus = delete_template(request, Profile, profile_id)
    return Response(data, status=HttpStatus)


@swagger_auto_schema(request_body=ProfileSerializer, method='POST')
@api_view(['POST'])
def login_profile_api(request):
    data, HttpStatus = login_check(request.data, ProfileSerializer)
    return Response(data, status=HttpStatus)


# BRANCHES API
@api_view(['GET'])
def get_branch_api(request, branch_id=None):
    serializer = BranchSerializer
    if branch_id is not None:
        data = get_one_template(request, Branches, serializer, branch_id)
        return Response({"data": data}, status=status.HTTP_200_OK)
    else:
        data = get_template(request, Branches, serializer)
        return Response({"data": data}, status=status.HTTP_200_OK)
    
@swagger_auto_schema(request_body=BranchSerializer, method='POST')
@api_view(['POST'])
def add_branch_api(request):
    data, HttpStatus = post_template(request, BranchSerializer)
    return Response(data, status=HttpStatus)

@swagger_auto_schema(request_body=BranchSerializer, method='PUT')
@api_view(['PUT'])
def update_branch_api(request, branch_id):
    data, HttpStatus = put_template(request, Branches, BranchSerializer, branch_id)
    return Response(data, status=HttpStatus)

@api_view(['DELETE'])
def delete_branch_api(request, branch_id):
    data, HttpStatus = delete_template(request, Branches, branch_id)
    return Response(data, status=HttpStatus)
