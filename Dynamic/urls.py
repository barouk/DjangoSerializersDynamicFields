from django.urls import path
from . import views

# from .views import CoustomTokenObtainPairView

urlpatterns = [
    path('DynamicModelView/', views.DynamicModelViews.as_view({"get":"list"}), name='DynamicModelViewset'),
    path('DynamicModelView/<int:pk>/', views.DynamicModelViews.as_view({"get": "retrieve"}), name='DynamicModelViewset'),

    path('DynamicViewset/', views.DynamicViews.as_view({"get": "list"}), name='DynamicViewset'),



]
