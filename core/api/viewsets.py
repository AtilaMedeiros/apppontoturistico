# from crypt import methods

from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico

from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse

#from rest_framework.response import Response
#from rest_framework.templatetags.rest_framework import add_query_param
#from multiprocessing.managers import Token


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer

    #permission_classes = (IsAuthenticated, )
    #permission_classes = (IsAdminUser, )
    #permission_classes = (IsAuthenticatedOrReadOnly, )
    #permission_classes = (DjangoModelPermissions, )
    #authentication_casses = (TokenAuthentication, )

    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'endereco__linha1')
    lookup_field = 'id'

    def get_queryset(self):
        # return PontoTuristico.objects.filter(aprovado=True)
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome=nome)

        if descricao:
            queryset = queryset.filter(descricao=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        # return Response({'teste': 123})
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # return Response({'Hello': request.data['nome']})
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # pass
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        # pass
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # pass
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        # pass
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    # detail = a True retorna o pk

    @action(detail=True, methods=['post', 'get'])
    def denunciar(self, request, pk=None):
        pass

    @action(detail=False, methods=['get'])
    def teste(self, request, pk=None):
        pass

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=id)

        ponto.atracoes.set(atracoes)

        ponto.save()
        return HttpResponse('OK')
