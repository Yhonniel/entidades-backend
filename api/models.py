from django.db import models
import uuid

class TipoDocumento(models.Model):
    codigo = models.CharField(
        max_length=20,
        verbose_name="Código"
    )
    nombre = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )
    descripcion = models.TextField(
        verbose_name='Descripción'
    )
    estado = models.BooleanField(
        verbose_name=('Estado'),
        default=True)

    def __str__(self):
        return '{0} - {1}'.format(self.codigo, self.nombre)

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipo de Documentos'


class TipoContribuyente(models.Model):
    nombre = models.CharField(
        max_length=50, verbose_name='Nombre'
    )
    estado = models.BooleanField(
        verbose_name=('Estado'),
        default=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de Contribuyente'
        verbose_name_plural = 'Tipo de Contribuyentes'


class Entidad(models.Model):
    tipo_documento = models.ForeignKey(
        TipoDocumento,
        on_delete=models.CASCADE,
        verbose_name='Tipo de documento'
    )
    numero_documento = models.CharField(
        max_length=40,
        verbose_name='Numero de documento'
    )
    razon_social = models.CharField(
        max_length=40,
        verbose_name='Razón Social'
    )
    tipo_contribuyente = models.ForeignKey(
        TipoContribuyente,
        on_delete=models.CASCADE,
        verbose_name='Tipo de Contribuyente'
    )
    nombre_comercial = models.CharField(
        max_length=150,
        verbose_name='Nombre Comercial'
    )
    telefono = models.CharField(
        max_length=50,
        verbose_name="Teléfono"
    )
    direccion = models.TextField(
        verbose_name='Dirección'
    )
    estado = models.BooleanField(
        verbose_name=('Estado'),
        default=True
    )

    def __str__(self):
        return '{0} {1} {2} '.format(self.tipo_documento, self.numero_documento, self.tipo_contribuyente)

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'