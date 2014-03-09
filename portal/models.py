from django.db import models
from portal.manager import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Categories(models.Model):
	categori = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.categori

class Tutorial(models.Model):
	categories = models.ForeignKey(Categories, null=True)
	title = models.CharField(max_length = 100)
	isi = models.TextField()
	created = models.DateTimeField()
	updated = models.DateTimeField(null=True)
	published = models.BooleanField(db_index = True, default = True)
	createby = models.CharField(max_length = 44)

	objects = EntryManager()

	def __unicode__(self):
		return u'%s' % (self.title)

class Comment(models.Model):
	tutorial = models.ForeignKey(Tutorial, null=True)
	Comment = models.TextField()
	name = models.CharField(max_length = 30)
	email = models.EmailField()
	website = models.CharField(max_length = 30, null = True)
	ip = models.CharField(max_length=30)
	datecoment = models.DateTimeField(auto_now_add = True)

	objects = KomentManager()

	def __unicode__(self):
		return u'%s' % (self.email)

class Contact(models.Model):
	nama = models.CharField(max_length = 30)
	email = models.EmailField()
	message = models.TextField(max_length = 60)

	def __unicode__(self):
		return u'%s' % (self.email)

class Visitor(models.Model):
	alamat = models.CharField(max_length = 60)
	browser = models.CharField(max_length = 60)
	operating = models.TextField(max_length = 60)
	view = models.DateTimeField(null = True)

	def __unicode__(self):
		return u'%s' % (self.alamat)

class Blogrol(models.Model):
	name = models.CharField(max_length = 40)
	link = models.CharField(max_length = 50)
	iconf = models.CharField(max_length = 100, blank = True)



