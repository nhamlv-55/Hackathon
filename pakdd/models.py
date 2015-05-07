from django.db import models
from django import forms
# Create your models here.

class ModelNN(models.Model):
	ItemId = models.AutoField(primary_key = True)
	Module = models.IntegerField()
	Part = models.IntegerField()
	Date = models.IntegerField()
	Value = models.IntegerField()

	def __unicode__(self):
		return '%s %s %s %s'%(self.Module, self.Part, self.Date, self.Value)

class ModelShize(models.Model):
	ItemId = models.AutoField(primary_key = True)
	Module = models.IntegerField()
	Part = models.IntegerField()
	Date = models.IntegerField()
	Value = models.FloatField()

	def __unicode__(self):
		return '%s %s %s %s'%(self.Module, self.Part, self.Date, self.Value)

class OldSet(models.Model):
	ItemId = models.AutoField(primary_key = True)
	Module = models.IntegerField()
	Part = models.IntegerField()
	Date = models.IntegerField()
	Value = models.IntegerField()

	def __unicode__(self):
		return '%s %s %s %s'%(self.Module, self.Part, self.Date, self.Value)
