from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import CustomUser
from .models import Advertisement
from .serializer import AdvertisementSerializer, CreateAdvertisementSerializer
from rest_framework import status


class AllAdvertisementAPIView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Advertisement.objects.all()
        serializer = AdvertisementSerializer(qs, many=True)
        return Response({'data': serializer.data})

class AdvertisementAPIView(APIView):
    def post(self, request, *args, **kwargs):
        account = kwargs.get('account')
        user = get_object_or_404(CustomUser, nickname=account)

        try:  # 해당 닉네임의 프로필이 이미 존재하는 경우
            instance = Advertisement.objects.get(post_account=user)
        except Advertisement.DoesNotExist:
            instance = None
        serializer = CreateAdvertisementSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save(post_account=user)
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, *args, **kwargs):
        account = kwargs.get('account')
        instance = Advertisement.objects.get(post_account__nickname=account)
        serializer = AdvertisementSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, *args, **kwargs): #update
        account = kwargs.get('account')
        instance = Advertisement.objects.get(post_account__nickname=account)
        serializer = AdvertisementSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        account = kwargs.get('account')
        instance = Advertisement.objects.get(post_account__nickname=account)
        instance.delete()
        return Response({'message': 'The object has been deleted'})

