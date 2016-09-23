from django.db import models

available_titles = (
		('MR', 'Mr.'),
		('RS', 'Mrs.'),
		('MS', 'Ms.'),
		('NA', 'N/A') )

available_meals = (
		('F', 'Filet Mignon'),
		('C', 'Chicken'),
		('V', 'Vegetarian') )

class Person(models.Model):
	title = models.CharField(max_length=2, choices=available_titles, default='MR')
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50, default='')
	attending = models.BooleanField(default=True)

	meal = models.CharField(max_length=1, choices=available_meals, default='F')

	def __str__(self):
		title = dict(available_titles)[self.title]
		meal = dict(available_meals)[self.meal]
		attending = 'will' if self.attending else 'will not'
		return ' '.join([title, self.first_name, self.last_name, attending, 'be attending.', meal])
