from django.db import models

class KomentManager(models.Manager):
	def Komentar(self):
		return self.model.objects.all()

class EntryManager(models.Manager):
	def Masukan(self):
		return self.model.objects.all().order_by('-created')[:6]
	#def Specific(self, id):
		#return self.model.objects.filter(id = id)
