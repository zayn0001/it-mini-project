from rest_framework import serializers
from .models import *


class getUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',"username","email", "phone")

class getAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ("first_name","last_name","username","email")



class createUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")

class createAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ("__all__")



class getPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ("__all__")

class getActivePackageSerializer(serializers.ModelSerializer):
    #package = serializers.CharField(read_only=True, source='package.name')
    #description = serializers.CharField(read_only=True, source='package.description')
    package = getPackageSerializer()
    class Meta:
        model = ActivePackage
        fields = ('__all__')

class DeactivateSerializer(serializers.Serializer):
    package = serializers.CharField(max_length = 50)

class createReviewSerializer(serializers.Serializer):
    package = serializers.CharField(max_length = 50)
    username = serializers.CharField(max_length = 50)
    description = serializers.CharField(max_length=400)

class createPackageSerializer(serializers.ModelSerializer):
    admin = serializers.CharField(max_length = 50)
    class Meta:
        model = Package
        fields = ("__all__")

class getReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True, source='user.username')
    class Meta:
        model = Review
        fields = ("user","description")

class ApplyPackageSerializer(serializers.Serializer):
    activepackage = serializers.CharField(max_length = 50)
    username = serializers.CharField(max_length = 50)

class activatePackageSerializer(serializers.Serializer):
    package = serializers.CharField(max_length = 50)
    class Meta:
        model = ActivePackage
        fields = ("__all__")


