from django.contrib.auth.models import User, Group
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from rest_framework import generics
from catalog.serializers import AssetSerializer, AssetClassSerializer, AssetDetailSerializer, UserSerializer, GroupSerializer
from catalog.models import Asset, AssetClass


class AssetList(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class AssetClassList(generics.ListCreateAPIView):
    queryset = AssetClass.objects.all()
    serializer_class = AssetClassSerializer

def details(request, pk):
    try:
        asset_item = Asset.objects.get(aname=pk)
    except Asset.DoesNotExist:
        raise Http404("Asset does not exist")

    if request.method == 'GET':
        serializer = AssetDetailSerializer(asset_item)
        return JsonResponse(serializer.data)

    #return render(request, 'asset/detail.html', {'asset_name': asset_item.aname, 'asset_type': asset_item.atype, 'asset_class': asset_item.aclass, 'asset_class_details' : asset_item.aclass.acdetails})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer