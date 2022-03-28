from django.urls import path
from .views import TipoDocumentoListAPIView, TipoDocumentoDetailAPIView, TipoContribuyenteListAPIView, \
    EntidadListAPIView, EntidadDetailAPIView, TipoContribuyenteDetailAPIView

urlpatterns = [
    path('tipo-documentos/', TipoDocumentoListAPIView.as_view(),  # listar, crear
         name='tipo-documentos'),

    path('tipo-documento/<int:pk>/', TipoDocumentoDetailAPIView.as_view(),  # de detalle actualizar y eliminar,
         name='tipo-documento'),

    path('tipo-contribuyentes/', TipoContribuyenteListAPIView.as_view(),
         name='tipo-contribuyentes'),

    path('tipo-contribuyente/<int:pk>/', TipoContribuyenteDetailAPIView.as_view(),
         name='tipo-contribuyente'),

    path('entidades/', EntidadListAPIView.as_view(),
         name='entidades'),

    path('entidad/<int:pk>/', EntidadDetailAPIView.as_view(),
         name='entidad'),
]
