from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentarios
from comentarios.api.serializers import ComentariosSerializer


class ComentarioViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer
