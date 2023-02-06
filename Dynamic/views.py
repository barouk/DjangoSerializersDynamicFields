from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.



class DynamicModelViews(viewsets.ModelViewSet):
    queryset = models.TestModel.objects.all()
    serializer_class = serializers.DynamicSerializer

    def get_serializer_context(self, *args, **kwargs):
        context = super().get_serializer_context()
        if self.action == 'list':
            context.update({"fields": ("id","field1")})
        return context



class DynamicViews(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        queryset = models.TestModel.objects.all()
        serializer_class = serializers.DynamicSerializer(queryset , many=True , context={'fields': ('field1',)})
        return Response(serializer_class.data)


