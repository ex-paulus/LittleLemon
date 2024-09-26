from .models import *
from .serializers import *
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   #permission_classes = [permissions.IsAuthenticated]    

def index(request):
    return render(request, 'index.html', {})