from django.db import models

class Lint(models.Model):
	title = models.CharField(max_length=255)
	cifra = models.IntegerField()
	def __str__(self):
		return self.title