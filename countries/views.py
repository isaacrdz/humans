from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import loader

from .models import Country
# Create your views here.
def country_list(request):
	country = Country.objects.order_by('id')
	template = loader.get_template('country.html')
	context = {
		"country": country
	}
	return HttpResponse(template.render(context,request))
