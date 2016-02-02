from commons.models import S_Province, S_City, S_District #@UnresolvedImport
from django.http.response import HttpResponse
from django.core import serializers

# Create your views here.
def get_province(request):
    provinces = S_Province.objects.all();
    provinces_json = serializers.serialize("json", provinces)
    return HttpResponse(provinces_json, content_type="application/json")
    

def get_city_by_province(request, province=""):
    citys = S_City.objects.filter(Province = int(province));
    citys_json = serializers.serialize("json", citys)
    return HttpResponse(citys_json, content_type="application/json")
    
    
def get_district_by_city(request, city=""):
    districts = S_District.objects.filter(City = int(city));
    districts_json = serializers.serialize("json", districts)
    return HttpResponse(districts_json, content_type="application/json")