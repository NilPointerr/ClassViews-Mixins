from rest_framework import serializers
from .models import User1
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User1
        fields = "__all__"  