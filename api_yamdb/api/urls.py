from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

API_VER: str = 'v1'

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet)
router_v1.register('genres', GenreViewSet)
router_v1.register('titles', TitleViewSet)

urlpatterns = [
    path(f'{API_VER}/', include(router_v1.urls)),
]
