from django.db import models

class Feedback(models.Model):
	full_name = models.CharField(max_length = 100,verbose_name= ('Title'))
	email = models.EmailField(verbose_name=('Email'))
	title = models.CharField(max_length = 50,verbose_name= ('Title'))
	content = models.TextField(verbose_name= ('Content'))

	def __str__(self):
		return self.title
