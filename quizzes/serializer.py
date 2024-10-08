from rest_framework import serializers

# create a serializer
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 15)
    password = serializers.CharField(max_length = 15)
    
