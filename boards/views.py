# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import BoardSerializer, citySerializer,contactSerializer
from app.models import contact_tble
from .models import BillBoard
from rest_framework import generics
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse


# Create your views here.
class listboards(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = BillBoard.objects.all()

    def list(self, request):
        queryset = BillBoard.objects.all()
        serializer = BoardSerializer(queryset, many=True)
        return Response(serializer.data)
    

class listCities(viewsets.ModelViewSet):
    serializer_class = citySerializer
    queryset = BillBoard.objects.all()

class listconatct(viewsets.ModelViewSet):
    serializer_class = contactSerializer
    queryset = contact_tble.objects.all()


def handler(request):
    if request.method == 'POST':
        print(request.POST.get('city'))
        print(request.POST.get('backLight'))
        print(request.POST.get('available'))
        serializer = BoardSerializer(o)
        return Response(serializer.data)
    return HttpResponse()
    