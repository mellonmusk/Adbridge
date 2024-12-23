from django.urls import path
from . import views
from knox.views import LogoutView
urlpatterns = [
    path('register/', views.CreateUserAPI.as_view()),
    path('update-user/<int:pk>/', views.UpdateUserAPI.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('advertiser-profile/', views.CreateAdvertiserProfileAPIView.as_view()), # 생성 및 전체 조회
    path('influencer-profile/', views.CreateInfluencerProfileAPIView.as_view()), # 생성 및 전체 조회
    path('influencer-profile/<int:pk>/', views.InfluencerProfileAPIView.as_view()), # 조회 및 수정
    path('advertiser-profile/<int:pk>/', views.AdvertiserProfileAPIView.as_view()),
]
