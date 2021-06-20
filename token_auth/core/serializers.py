from rest_framework import serializers
from .models import register

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = register
        #fields = '__all__'
        fields =['first_name','last_name','mobile','email','state','district','village','block']
