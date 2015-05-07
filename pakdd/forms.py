import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from models import *

class SearchForm(forms.Form):
	module = forms.ChoiceField(choices = [(x,x) for x in range(1,10)])
	part = forms.ChoiceField(choices = [(x,x) for x in range(1,32)])
	algo = forms.ChoiceField(choices = [("Model1", 1), ("Model2",2), ("Model3",3)])