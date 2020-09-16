# es necesario el include para la lista de urls del viewset
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfilesViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
     path('hello-view/', views.HelloApiView.as_view()),
     # ver la propiedad urls que generan las viewset
     path('login/', views.UserLoginApiView.as_view()),
     path('', include(router.urls))
]

