from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
	content = models.FileField(null=True, blank=True)

	def __unicode__(self):
		return self.content

	def __str__(self):
		return self.title
