from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.viewsets import GenericViewSet


class GetCreateDeleteMixin(CreateModelMixin, ListModelMixin,
                           DestroyModelMixin, GenericViewSet):
    """Mixin class for get, create or delete objects."""
    pass
