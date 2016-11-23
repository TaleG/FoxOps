from django.shortcuts import render,HttpResponse
import json

from foxcmdb import models
from foxcmdb import tables
from foxcmdb import admin
from foxcmdb import asset_handle
from foxcmdb import utils
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def asset(request):
    asset_list = models.Asset.objects.all()
    return render(request,'cmdb/asset.html',{'asset_list':asset_list})

def host(request):
    print(request.GET)
    asset_obj_list = tables.table_filter(request, admin.AssetAdmin, models.Asset)
    # asset_obj_list = models.Asset.objects.all()
    print("asset_obj_list:", asset_obj_list)
    order_res = tables.get_orderby(request, asset_obj_list, admin.AssetAdmin)
    # print('----->',order_res)
    paginator = Paginator(order_res[0], admin.AssetAdmin.list_per_page)

    page = request.GET.get('page')
    try:
        asset_objs = paginator.page(page)
    except PageNotAnInteger:
        asset_objs = paginator.page(1)
    except EmptyPage:
        asset_objs = paginator.page(paginator.num_pages)

    table_obj = tables.TableHandler(request,
                                    models.Asset,
                                    admin.AssetAdmin,
                                    asset_objs,
                                    order_res
                                    )

    return render(request, 'cmdb/host_list.html', {'table_obj': table_obj,
                                                  'paginator': paginator})

def get_asset_list(request):
    asset_dic = asset_handle.fetch_asset_list()
    print(asset_dic)

    return HttpResponse(json.dumps(asset_dic, default=utils.json_date_handler))
