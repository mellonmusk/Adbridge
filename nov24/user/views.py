from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from knox import views as knox_views
from .models import AdvertiserProfile, InfluencerProfile, CustomUser
from .serializer import CreateUserSerializer, UpdateUserSerializer, AdvertiserProfileSerializer, \
    InfluencerProfileSerializer, LoginSerializer, CreateAdvertiserProfileSerializer, CreateInfluencerProfileSerializer
from rest_framework import status
from django.views import View

def hello(request):
    return render(request, 'logg/hello.html')



class SignUpPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/sign_up.html')

class CreateUserAPI(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

    # def post(self, request, *args, **kwargs):
    #     response = super().post(request, *args, **kwargs)
    #     return redirect('sign-up-page')

# class UpdateUserAPI(UpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UpdateUserSerializer

class LoginAPIView(knox_views.LoginView):
    permission_classes = (AllowAny,)
    serializer_class= LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response({'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response(response.data, status=status.HTTP_200_OK)



# 광고주
class AdvertiserProfileAPIView(APIView): #전체 조회
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration/advertiser-profile-list.html'
    def get(self, request, *args, **kwargs):
        qs = AdvertiserProfile.objects.all()
        serializer = AdvertiserProfileSerializer(qs, many=True)
        return Response({'profiles': serializer.data})
class CreateAdvertiserProfileAPIView(APIView): # 생성, 조회, 수정
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration/one-advertiser-profile.html'
    def post(self, request, *args, **kwargs):
        account = kwargs.get('account')
        user = get_object_or_404(CustomUser, nickname=account)
        try:  # 해당 닉네임의 프로필이 이미 존재하는 경우
            instance = AdvertiserProfile.objects.get(post_account=user)
        except AdvertiserProfile.DoesNotExist:
            instance = None

        serializer = CreateAdvertiserProfileSerializer(instance=instance, data=request.data)

        if serializer.is_valid():
            serializer.save(post_account=user)
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        account = kwargs.get('account')
        instance = AdvertiserProfile.objects.get(post_account__nickname=account)
        serializer = AdvertiserProfileSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            return Response({'profile': serializer.data, 'account':account})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs): #update
        account = kwargs.get('account')
        instance = AdvertiserProfile.objects.get(post_account__nickname=account)
        serializer = AdvertiserProfileSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# 인플루언서
class InfluencerProfileAPIView(APIView): #전체 조회
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration/influencer-profile-list.html'
    def get(self, request, *args, **kwargs): #전체 생성된 인플루언서 프로필 조회
        qs = InfluencerProfile.objects.all()
        serializer = InfluencerProfileSerializer(qs, many=True)
        return Response({'profiles': serializer.data})

class CreateInfluencerProfileAPIView(APIView): # 생성, 조회, 수정
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'registration/one-influencer-profile.html'
    def post(self, request, *args, **kwargs): #생성
        account = kwargs.get('account')
        user = get_object_or_404(CustomUser, nickname=account)
        try: #해당 닉네임의 프로필이 이미 존재하는 경우
            instance = InfluencerProfile.objects.get(post_account=user)
        except InfluencerProfile.DoesNotExist:
            instance = None

        serializer = CreateInfluencerProfileSerializer(instance=instance, data=request.data)

        if serializer.is_valid():
            serializer.save(post_account=user)
            #return Response({'data': serializer.data})
            return redirect('influencer-profile-detail', account=account)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs): #조회
        account = kwargs.get('account')
        instance = InfluencerProfile.objects.get(post_account__nickname=account)
        serializer = InfluencerProfileSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            return Response({'profile': serializer.data, 'account':account})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):  # update
        account = kwargs.get('account')
        instance = InfluencerProfile.objects.get(post_account__nickname=account)
        serializer = InfluencerProfileSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

