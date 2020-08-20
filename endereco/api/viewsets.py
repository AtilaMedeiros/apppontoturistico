from rest_framework.viewsets import ModelViewSet
from endereco.models import Endereco
from endereco.api.serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
