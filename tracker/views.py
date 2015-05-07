from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response, render, get_object_or_404
# from tracker.forms import *
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

def loan_shark(request):
	query="muse"
	if request.GET.has_key('query'):
		query = request.GET['query'].strip()
	
	variables = RequestContext(request, {
		'query': query
		# 'content': str(content)
		})
	return render_to_response('loan_shark.html', variables)


	variables=RequestContext(request, {
		'id':id
		})
	return render_to_response('loan_shark.html')


def map(request):
	return render_to_response('map.html')
def test(request):
	return render_to_response('barchart.html')
def q2(request):
	return render_to_response('q2.html')
def creative(request):
	return render_to_response('creative.html')