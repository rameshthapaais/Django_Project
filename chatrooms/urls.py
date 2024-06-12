from rest_framework.routers import DefaultRouter
from .viewsets import *

router = DefaultRouter()
router.register('chatroom', ChatRoomViewsets, basename='chatroom')
router.register('message', MessageViewsets, basename='message')
urlpatterns = router.urls