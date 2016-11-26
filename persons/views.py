from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import loader

from .models import Person

# Create your views here.
def person_list(request):
	person = Person.objects.order_by('id')
	template = loader.get_template('persons.html')
	context = {
		"person": person
	}
	return HttpResponse(template.render(context, request))