from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import loader

from .models import State
# Create your views here.
def state_list(request):
	state = State.objects.order_by('id')
	template = loader.get_template('state.html')
	context = {
		"state": state
	}
	return HttpResponse(template.render(context,request))