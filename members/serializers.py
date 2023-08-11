from rest_framework import serializers
from .models import Profile, Church

class ChurchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Church
        fields = ['minister_name', 'church_name', 'city', 'state', 'country']

class ProfileSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'profile_picture', 'birthdate', 'phone_area_code', 'phone_number', 'voice_type', 'role']
