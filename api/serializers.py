from .models import TipoDocumento, TipoContribuyente, Entidad
from rest_framework import serializers


class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = (
            'pk',
            'codigo',
            'nombre',
            'descripcion',
            'estado',
        )


class TipoContribuyenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContribuyente
        fields = (
            'pk',
            'nombre',
            'estado',
        )


class EntidadSerializer(serializers.ModelSerializer):
    tipo_documento = TipoDocumentoSerializer(read_only=True)
    tipo_documento_id = serializers.IntegerField(write_only=True)

    tipo_contribuyente = TipoContribuyenteSerializer(read_only=True)
    tipo_contribuyente_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Entidad
        fields = (
            'pk',
            'tipo_documento',
            'tipo_documento_id',
            'tipo_contribuyente',
            'tipo_contribuyente_id',
            'numero_documento',
            'razon_social',
            'nombre_comercial',
            'telefono',
            'direccion',
            'estado',
        )
