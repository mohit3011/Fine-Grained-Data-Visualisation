from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
	content = models.FileField(null=True, blank=True)

	def __unicode__(self):
		return self.content

	def __str__(self):
		return self.content


class Post1(models.Model):
	hash1 = models.CharField(max_length=100)
	hash2 = models.CharField(max_length=100)
	hash3 = models.CharField(max_length=100)


	def __unicode__(self):
		return self.hash1

	def __str__(self):
		return self.hash1
