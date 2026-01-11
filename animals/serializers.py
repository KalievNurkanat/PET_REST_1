from rest_framework import serializers
from animals.models import Animal, Category
from users.models import CustomUser

class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username"]


# Animal
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ["id", "title"]

class AnimalDetailSerializer(serializers.ModelSerializer):
     author = UserBaseSerializer(read_only=True)
     class Meta:
          model = Animal
          fields = "__all__"

# category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title"]

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    
               
          
          