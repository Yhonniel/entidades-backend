from django.contrib import admin

from api.models import TipoDocumento,TipoContribuyente,Entidad



@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'descripcion', 'estado')


@admin.register(TipoContribuyente)
class TipoContribuyenteAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'estado')


@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'tipo_documento', 'numero_documento', 'razon_social', 'tipo_contribuyente', 'nombre_comercial', 'telefono',
    'direccion', 'estado')



