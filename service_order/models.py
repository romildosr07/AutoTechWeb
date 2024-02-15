import uuid

from django.db import models


class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Carro', max_length=100, null=True, blank=True)
    plate = models.CharField('Placa', max_length=100, null=True, blank=True)
    kms = models.IntegerField('KMs', null=True, blank=True)

    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('criado', auto_now_add=True)
    updated_at = models.DateTimeField('modificado', auto_now=True)

    class Meta:
        db_table = 'vehicle'
        verbose_name = 'veiculo'
        verbose_name_plural = 'veiculos'

    def __str__(self):
        return f'{self.plate}'


class ServiceOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField('Numero')

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='veiculo')

    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('Criado', auto_now_add=True)
    updated_at = models.DateTimeField('modificado', auto_now=True)

    class Meta:
        db_table = 'service_order'
        verbose_name = 'ordem de serviço'
        verbose_name_plural = 'ordens de serviços'

    def __str__(self):
        return f'OS: {self.number}'


class PartOrServiceType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Tipo', max_length=50)

    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('criado', auto_now_add=True)
    updated_at = models.DateTimeField('modificado', auto_now=True)

    class Meta:
        db_table = 'part_or_service_type'
        verbose_name = 'tipo peça ou serviço'
        verbose_name_plural = 'tipos peças ou serviços'

    def __str__(self):
        return f'{self.name}'


class PartOrService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.IntegerField('Quantidade', null=True, blank=True)
    name = models.CharField('nome', max_length=100)
    value = models.DecimalField('Valor', max_digits=6, decimal_places=2)

    part_or_service_type = models.ForeignKey(PartOrServiceType, on_delete=models.SET_NULL, verbose_name='Tipo', null=True)
    service_order = models.ForeignKey(ServiceOrder, on_delete=models.CASCADE, verbose_name='Ordem de Serviço')

    is_active = models.BooleanField('Ativo', default=True)
    created_at = models.DateTimeField('criado', auto_now_add=True)
    updated_at = models.DateTimeField('modificado', auto_now=True)

    class Meta:
        db_table = 'part_or_service'
        verbose_name = 'peça ou serviço'
        verbose_name_plural = 'peças ou serviços'

    def __str__(self):
        return f'{self.name}'
