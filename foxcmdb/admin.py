# _*_ coding:utf-8 _*_
from django.contrib import admin

from foxcmdb import models

# Register your models here.


class ServerInline(admin.TabularInline):
    model = models.Server
    exclude = ('memo',)
    readonly_fields = ['create_date']

class CPUInline(admin.TabularInline):
    model = models.CPU
    exclude = ('memo',)
    readonly_fields = ['creat_date']
class NICInline(admin.TabularInline):
    model = models.NIC
    exclude = ('memo',)
    readonly_fields = ['create_date']
class RAMInline(admin.TabularInline):
    model = models.RAM
    exclude = ('memo',)
    readonly_fields = ['create_date']
class DiskInline(admin.TabularInline):
    model = models.Disk
    exclude = ('memo',)
    readonly_fields = ['create_date']

class AssetAdmin(admin.ModelAdmin):
    list_display = ('id','asset_type','sn','name','manufactory','management_ip','idc','business_unit','admin')
    inlines = [ServerInline,CPUInline,RAMInline,DiskInline,NICInline]
    search_fields = ['sn',]
    list_filter = ['idc','manufactory','business_unit','asset_type']
    choice_fields = ('asset_type','status')
    fk_fields = ('manufactory','idc','business_unit','admin')
    list_per_page = 10
    #list_filter = ('asset_type','status','manufactory','idc','business_unit','admin','trade_date')
    dynamic_fk = 'asset_type'
    dynamic_list_display = ('model','sub_asset_type','os_type','os_distribution')
    dynamic_choice_fields = ('sub_asset_type',)
    m2m_fields = ('tags',)


class NicAdmin(admin.ModelAdmin):
    list_display = ('name','macaddress','ipaddress','netmask','bonding')
    search_fields = ('macaddress','ipaddress')


class EventLogAdmin(admin.ModelAdmin):
    list_display = ('name','colored_event_type','asset','component','detail','date')
    search_fields = ('asset',)
    list_filter = ('event_type','component','date')

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect


class NewAssetApprovalZoneAdmin(admin.ModelAdmin):
    list_display = ('sn','asset_type','manufactory','model','cpu_model','cpu_count','cpu_core_count','ram_size','os_distribution','os_release','date','approved','approved_by','approved_date')
    actions = ['approve_selected_objects']
    def approve_selected_objects(modeladmin, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        ct = ContentType.objects.get_for_model(queryset.model)
        return HttpResponseRedirect("/asset/new_assets/approval/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))
    approve_selected_objects.short_description = "批准入库"



admin.site.register(models.Asset,AssetAdmin)
admin.site.register(models.Contract)
admin.site.register(models.BusinessUnit)
admin.site.register(models.CPU)
admin.site.register(models.EventLog,EventLogAdmin)
admin.site.register(models.Disk)
admin.site.register(models.Manufactory)
admin.site.register(models.NIC,NicAdmin)
admin.site.register(models.Server)
admin.site.register(models.RAM)
admin.site.register(models.Tag)
admin.site.register(models.Software)
admin.site.register(models.NewAssetApprovalZone,NewAssetApprovalZoneAdmin)
admin.site.register(models.NetworkDevice)
admin.site.register(models.IDC)