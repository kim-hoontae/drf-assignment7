from rest_framework import serializers

from users.models import User

class SignupSerializers(serializers.ModelSerializer):
    class Meta:
        model        = User
        fields       = ('email','name','password')
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user