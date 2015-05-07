from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response, render, get_object_or_404
from pakdd.forms import *
import urllib2
import re
import time
import csv
import os


# ----------------------------------------------------------------
def main_page(request):
	query="muse"
	if request.GET.has_key('query'):
		query = request.GET['query'].strip()
	
	variables = RequestContext(request, {
		'query': query
		# 'content': str(content)
		})
	return render_to_response('main.html', variables)


	variables=RequestContext(request, {
		'id':id
		})
	return render_to_response('main.html')

def result(request):
	form = SearchForm()
	old=[]
	value = []
	show_results = False
	if request.GET.has_key('module'):
		show_results = True
		m = request.GET['module']
		p = request.GET['part']
		# if len(p)==1:
			# p="0"+p
		tmpOld = OldSet.objects.filter(Module = m, Part = p)
		a = request.GET['algo']
		if a=="1":
			tmp = ModelNN.objects.filter(Module = m, Part = p)
		elif a=="2":
			tmp = ModelShize.objects.filter(Module = m, Part = p)
		for item in tmp:
			value.append(int(item.Value))
		for item in tmpOld:
			old.append(int(item.Value))
	variables = RequestContext(request, {
		'old': old,
		'value': value,
		'form': form,
		'show_results': show_results,
		'm': m,
		'p': p,
		'a': a,
		})
	return render_to_response('pakdd/result.html', variables)
def pakdd(request):	
	form = SearchForm()
	variables = RequestContext(request, {
		'form': form,
		# 'content': str(content)
		})
	return render_to_response('pakdd/home.html', variables)


def map(request):
	return render_to_response('map.html')
def test(request):
	return render_to_response('barchart.html')
def q2(request):
	return render_to_response('q2.html')
def creative(request):
	return render_to_response('creative.html')