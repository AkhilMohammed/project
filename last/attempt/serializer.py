
from rest_framework import serializers

from attempt.models import User



class signupserializer(serializers.ModelSerializer):

    class META:

        model =User

        fields =['firstname' ,'lastname' ,'gender' ,'email' ,'mobile']

