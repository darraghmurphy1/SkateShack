from django.shortcuts import render
from django.core import serializers
import json
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    json_products = serializers.serialize('json', products)
    return HttpResponse(json_products, content_type='application/json')

def category_list(request):
    categories = Category.objects.all()
    json_categories = serializers.serialize('json', categories)
    return HttpResponse(json_categories, content_type='application/json')