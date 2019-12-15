from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from urllib.parse import urlencode
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    fieldnames = ['ID', 'Name', 'Longitude_WGS84', 'Latitude_WGS84', 'Street', 'AdmArea', 'District', 'RouteNumbers',
                  'StationName', 'Direction', 'Pavilion', 'OperatingOrgName', 'EntryState', 'global_id', 'geoData']

    with open(settings.BUS_STATION_CSV, encoding='cp1251') as f:
        f.readline()
        reader = csv.DictReader(f, fieldnames=fieldnames)
        result = list(reader)

    paginator = Paginator(result, 10)
    current_page = int(request.GET.get('page', 1))

    if current_page > paginator.num_pages:
        current_page = paginator.num_pages

    try:
        page = paginator.get_page(current_page)
        data = page.object_list
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
        data = page.object_list

    next_page, next_page_url = None, None

    if page.has_next():
        next_page = paginator.page(current_page).next_page_number()
        next_page_url = f'http://127.0.0.1:8000{reverse("bus_stations")}?{urlencode({"page": next_page})}'

    return render_to_response("index.html", context={
        'bus_stations': data,
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })

