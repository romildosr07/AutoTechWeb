from django.contrib import admin

from service_order.models import Vehicle, PartOrServiceType, PartOrService, ServiceOrder


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'plate', 'is_active')
    search_fields = ['id', 'vehicle', 'plate', 'is_active']


@admin.register(PartOrServiceType)
class PartOrServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    search_fields = ('id', 'name', 'is_active')


@admin.register(PartOrService)
class PartOrServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'name', 'value', 'is_active')
    search_fields = ('id', 'name', 'is_active')


class VehicleInline(admin.StackedInline):
    model = Vehicle
    extra = 0


class PartOrServiceInline(admin.TabularInline):
    model = PartOrService


@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ('os_number', 'vehicle_plate', 'created_at')

    @admin.display(description='numero OS')
    def os_number(self, obj):
        return obj.number

    @admin.display(description='placa')
    def vehicle_plate(self, obj):
        return obj.vehicle.plate

    inlines = [PartOrServiceInline]


