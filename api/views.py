from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import TipoDocumento, TipoContribuyente, Entidad
from .serializers import TipoDocumentoSerializer, TipoContribuyenteSerializer, EntidadSerializer


class TipoDocumentoListAPIView(ListCreateAPIView):
    queryset = TipoDocumento.objects.filter()
    serializer_class = TipoDocumentoSerializer
    permission_classes = (AllowAny,)


class TipoDocumentoDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TipoDocumento.objects.filter()
    serializer_class = TipoDocumentoSerializer
    permission_classes = (AllowAny,)


class TipoContribuyenteListAPIView(ListCreateAPIView):
    queryset = TipoContribuyente.objects.filter()
    serializer_class = TipoContribuyenteSerializer
    permission_classes = (AllowAny,)


class TipoContribuyenteDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TipoContribuyente.objects.filter()
    serializer_class = TipoContribuyenteSerializer
    permission_classes = (AllowAny,)


class EntidadListAPIView(ListCreateAPIView):
    queryset = Entidad.objects.filter()
    serializer_class = EntidadSerializer
    permission_classes = (AllowAny,)


class EntidadDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Entidad.objects.filter()
    serializer_class = EntidadSerializer
