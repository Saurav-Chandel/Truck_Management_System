from rest_framework import serializers
from .models import *


class SignUpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields="__all__"
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            # phone_number=validated_data['phone_number'],
            # phone_otp=validated_data['phone_otp']
        )
        user.set_password(validated_data['password'])
        user.save()
        # print(user.id)

        #create profile instance.
        profile_obj=Profile.objects.create(user_id=user.id)
        profile_obj.save()
        # print(profile_obj.User_id)

    
        return user


class DeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Devices
        fields="__all__"

    def create(self, validated_data):
        D=Devices.objects.create(**validated_data)
        return D

class AddVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Add_Vehicle
        fields="__all__"

    def crate(self,validated_data):
        AV=Add_Vehicle.objects.create(**validated_data)
        return AV    


class UpdatedDeiselPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Updated_Deisel_Price
        fields="__all__"

    def crate(self,validated_data):
        AV=Updated_Deisel_Price.objects.create(**validated_data)
        return AV   


class BackLoadMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Back_Load_Material
        fields="__all__"

    def crate(self,validated_data):
        AV=Back_Load_Material.objects.create(**validated_data)
        return AV           


class IncomePerRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Income_Per_Route
        fields="__all__"

    def crate(self,validated_data):
        AV=Income_Per_Route.objects.create(**validated_data)
        return AV   