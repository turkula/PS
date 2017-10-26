# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.


class blogPost(models.Model):
	title= models.CharField(max_length=150)
	body=models.TextField()
	time=models.DateTimeField()

class blogPostAdmin(admin.ModelAdmin):
	list_display=('title','time')

admin.site.register(blogPost,blogPostAdmin)		