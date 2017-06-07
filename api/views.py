# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.services.userservices import user_service


@api_view(["GET"])
def get_test(request):
    return Response(data="eeklesia", status=status.HTTP_200_OK)

@api_view(["POST"])
def create_user(request):
    user_data = request.data
    user = user_service.create_user(user_data)

    return Response(data=user, status=status.HTTP_201_CREATED)