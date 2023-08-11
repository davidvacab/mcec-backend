from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from rest_framework.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as BaseTokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from members.serializers import ProfileSerializer, ChurchSerializer
from members.models import Profile, Church

User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    profile = ProfileSerializer()
    church = ChurchSerializer()

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', 'password', 'email', 'profile', 'church']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        church_data = validated_data.pop('church')

        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        # user.is_active = False
        user.save()
        Profile.objects.create(user=user, **profile_data)
        Church.objects.create(user=user, **church_data)

        return user
    
    def validate(self, attrs):
        profile_data = attrs.pop('profile')
        profile = Profile(**profile_data)
        church_data = attrs.pop('church')
        church = Church(**church_data)
        user = User(profile=profile, church=church, **attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error[api_settings.NON_FIELD_ERRORS_KEY]}
            )
        
        attrs['profile'] = profile_data
        attrs['church'] = church_data

        return attrs

class UserSerializer(BaseUserSerializer):
    profile = ProfileSerializer()
    
    class Meta(BaseUserSerializer.Meta):
        fields = ['username', 'email', 'profile']
        

class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializer(self.user)
        data['user'] = serializer.data
        return data