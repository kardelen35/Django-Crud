from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class UserListCreateView(generics.ListCreateAPIView): #DRF'nin sağladığı hem listeleme (ListAPIView) hem de oluşturma (CreateAPIView) işlemlerini bir araya getiren bir view'dur.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class UserDetailView(generics.RetrieveUpdateDestroyAPIView): #DRF'nin sağladığı hem getirme (RetrieveAPIView), hem güncelleme (UpdateAPIView), hem de silme (DestroyAPIView) işlemlerini bir araya getiren bir view'dur.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class AllUsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    partial = True #partial = True: PATCH isteklerinde kısmi güncellemeye izin verir.
    
    
class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object() #Silinecek nesneyi alır.
        instance.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)