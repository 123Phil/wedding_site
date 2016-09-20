from django.db import models

class Person(models.Model):
	title = models.CharField(max_length=10)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	attending = models.CharField(max_length=80)
	meal = models.CharField(max_length=80)

	def __str__(self):
		attending = 'will' if self.attending else 'will not'
		return ' '.join(self.title, self.first_name, self.last_name, attending, 'be attending.', self.meal)
