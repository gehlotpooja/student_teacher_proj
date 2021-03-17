from django.core.mail import send_mail
from django.db.models import signals
from django.dispatch import receiver
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from student_teacher_app.controllers import *
from django.http import JsonResponse, Http404
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
# Create your views here.


@api_view(['POST'])
def create_user_api(request):
    try:
        data = create_user(request)
    except Exception as e:
        print(e.args)
    return Response(data=data,status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_user_api(request):
    try:
        data = update_user(request)
    except Exception as e:
        print(e.args)
    return Response(data = data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_details_with_id_api(request):
    try:
        data = get_user_details_with_id(request)
    except Exception as e:
        print(e.args)
    return Response(data=data,status=status.HTTP_200_OK)


@api_view(['GET'])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def get_all_user_details_api(request):
    try:
        data = get_all_user_details(request)
    except Exception as e:
        print(e.args)
    return JsonResponse(data, safe= False,status=200)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
# @permission_classes([IsAuthenticated])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@api_view(['POST'])
def verify(request):
    try:
        post_data = request.POST
        # uid = post_data['id']
        uid = 15
        user = User.objects.get(id=uid, is_staff=False)
    except User.DoesNotExist:
        raise Http404("User does not exist or is already verified")

    user.is_staff = True
    user.save()

    data = 'welcome'
    return Response(data=data,status=status.HTTP_200_OK)


