from django.urls import path, include
from .views import QuestViewSet, QCommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list', QuestViewSet)
router.register('qcomment', QCommentViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path('api/user/', include('accounts.urls')),
]