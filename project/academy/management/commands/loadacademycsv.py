import os
import csv
from django.conf import settings
from academy.models import Invite
from django.core.management.base import BaseCommand

class Command(BaseCommand):

	def handle(self, *args, **options):
		print "Loading CSV"
		# grabs the location of the csv and loads into var csv_path
		# os.path.join just gives the official location, which is why we put it next to manage.py
		csv_path = os.path.join(settings.BASE_DIR, "academy_invites_2014.csv")
		# opens and loads the csv into csv_file
		csv_file = open(csv_path, 'rb')
		# brings the csv into a python dictionary (import csv)
		csv_reader = csv.DictReader(csv_file)
		#deletes what's there
#		Invite.objects.delete
		# csv_reader is the name of the python list
		for row in csv_reader:
#			print row
			# Invite is the class name in models that we imported from academy.models 
			# objects are the rows in the csv
			# for each row, it will add row, assigning name in the row to name in the db etc
			obj = Invite.objects.create(
				name=row['Name'],
				branch=row['Branch']
			)
			print obj
