from animals.models import Animal, Category
from animals.serializers import (CategorySerializer,
                                  CategoryDetailSerializer, 
                                  AnimalSerializer, 
                                  AnimalDetailSerializer)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from common.permissions import IsAdmin, IsAuthenticated, IsOwner, IsGuest
# Create your views here.

class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsGuest | (IsAdmin & IsAuthenticated)]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CategorySerializer
        return CategoryDetailSerializer

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [(IsAdmin & IsAuthenticated) | IsGuest]
    serializer_class = CategoryDetailSerializer
    lookup_field = "id"


class AnimalView(ListCreateAPIView):
    queryset = Animal.objects.all()
    permission_classes = [IsAdmin | IsAuthenticated  | IsGuest]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AnimalSerializer
        return AnimalDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AnimalDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner | (IsAdmin & IsAuthenticated)]
    queryset = Animal.objects.all()
    serializer_class = AnimalDetailSerializer
    lookup_field = "id"



