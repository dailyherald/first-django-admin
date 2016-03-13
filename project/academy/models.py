from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Invite(models.Model):
	name = models.CharField(max_length=500)
	branch = models.CharField(max_length=500)

	# List of items to restrict choices
	GENDER_CHOICES = (
		("M", "Male"),
		("F", "Female"),
		("O", "Other"),
		("?", "Unknown")
	)
	# sets column in the model as one length, with choices restricted by var GENDER_CHOICES
	gender = models.CharField(
		max_length=1,
		choices=GENDER_CHOICES,
		default="?" # Default is unknown
	)
	date_of_birth = models.DateField(null=True, blank=True)
	RACE_CHOICES = (
		("ASIAN", "Asian"),
		("BLACK", "Black"),
		("LATINO", "Latino"),
		("WHITE", "White"),
		("OTHER", "Other"),
		("?", "Unknown"),
	)
	race = models.CharField(
		max_length=10,
		choices=RACE_CHOICES,
		default="?"
	)
	notes = models.TextField(blank=True)




