from django.db import models

class RsvpForm(models.Model):
	parts = []
	for i in range(5):
		parts.append({
				'attending': forms.RadioField()
				'title': forms.CharField(max_length=10)
				'first_name': forms.CharField(max_length=50)
				'last_name': forms.CharField(max_length=50)
				'attending': forms.BooleanField(required=False, default=True)
				'meal': forms.RadioField(labels=[' Filet Mignon', ' Chicken', ' Vegetarian'])
			})
