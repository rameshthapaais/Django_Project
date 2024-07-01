from rest_framework.routers import DefaultRouter
from .viewsets import *
from .views import *
from django.urls import path

router = DefaultRouter()
router.register('chatroom', ChatRoomViewsets, basename='chatroom')
router.register('message', MessageViewsets, basename='message')
urlpatterns = router.urls
urlpatterns += [
    path('sum_num/', sumNumbersView, name='sum_num'),
]
