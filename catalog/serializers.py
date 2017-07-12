from rest_framework import serializers
from catalog.models import Asset, AssetClass


from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Asset, AssetClass

class AssetSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Asset
        fields = ('aname', 'atype', 'aclass')


class AssetClassSerializer(serializers.ModelSerializer):
    #ast_object = AssetSerializer(many=True)  # This.

    class Meta:
        model = AssetClass
        fields = ('acclass', 'acdetails')

class AssetDetailSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Asset
        fields = ('aname', 'atype', 'aclass')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')