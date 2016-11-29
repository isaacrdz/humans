from __future__ import unicode_literals

from django.db import models

# Create your models here.
class State(models.Model):
	state = models.CharField(max_length=255,)

	def __str__(self):
		return self.state