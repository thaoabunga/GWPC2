import old_GWPC
import datetime
import sys
import pprint

print "+++Great Western Power Company's Fitness Calendar+++"
print "|Climbing | CrossFit | Yoga |"
print "520 20th St, Oakland, CA 94612"
print "Phone:(510) 452-2022""\n"


import time;
localtime = time.asctime( time.localtime(time.time()) )

print "Today is", localtime

import calendar

cal = calendar.month(2016, 3)
print "--------------------------""\n"
print cal

#the available classes for today are
#find a way to list classes for the date
print 'What are you interested in today?-->'"\n"

sys.stdout.flush()

def choice():
	print "(C)limbing or (Y)oga?-->"
	sys.stdout.flush()
	choices =raw_input()
	if choices=='Y' or choices=='y':
			year = '2016'
			yoga_classes = [yclass for yclass in old_GWPC.FitnessClasses if "Yoga" in yclass["class"]]

			#class_dates = [ yclass['time'] for yclass in yoga_classes]
			class_date_strs = [yclass['time'] for yclass in yoga_classes]

			class_dates = []
			for class_date_str in class_date_strs:
				#each class_date_str looks like 'Mar 30 @ 7:00 pm \xe2\x80\x93 8:15 pm'

				(date,_,rest) = class_date_str.partition(' @ ')

				#rest now looks like '7:00 pm \xe2\x80\x93 8:15 pm'


				from_time,_,to_time = rest.partition(' \xe2\x80\x93 ')

				#from_time now looks like '7:00 pm'
				#_ now looks like ' \xe2\x80\x93 '
				#to_time now looks like '8:15 pm'

				#from_time example: '2016 Mar 30 7:00 pm'
				from_date_time = year + ' ' + date + ' ' + from_time
				#to_time example: '2016 Mar 30 8:12 pm'
				to_date_time = year + ' ' + date + ' ' + to_time

				#from_date_time = from_date_time.replace('am', 'AM').replace('pm', 'PM')
				#to_date_time = to_date_time.replace('am', 'AM').replace('pm', 'PM')

				from_date_time = datetime.datetime.strptime(from_date_time, '%Y %b %d %I:%M %p')
				to_date_time = datetime.datetime.strptime(to_date_time, '%Y %b %d %I:%M %p')

				class_dates.append( (from_date_time, to_date_time) )

			print 'Select a time:-->'"\n\n"
			i = 1
			for (from_date_time,to_date_time) in class_dates:
				print ('%s.' % (i,) ), from_date_time.strftime('%b %d %I:%M %p'), '-', to_date_time.strftime('%b %d %I:%M %p')
				i += 1

			sys.stdout.flush()

			choices = raw_input()

			selection = int(choices) - 1

			(selection_date_from, selection_date_to) = class_dates[selection]

			print 'Namaste. Your Yoga class is from', selection_date_from.strftime('%b %d %I:%M %p'), '-', to_date_time.strftime('%b %d %I:%M %p')

			#class_dates = [datetime.strptime(class_date, '%b %d @ %I:%M %p \xe2\x80\x93 8:15 pm' + ' ' year) for class_date in class_dates]
			# newlist = []
			# newlist = sorted(yoga_classes, key=lambda k: k['time'])
			# s = 'Mar 10 @ 7:30 am'
			# ask user what time?
			# format = '%Y-%m-%d %H:%M:'
			# date=datetime.datetime.strptime(s, format)
			# date
			# datetime.datetime(2016, 3)

			#print yoga_classes
			#pprint.pprint(class_dates)
			#change yoga classes into data objects
			#sort yoga classes by date
			#print yoga classes by date
	elif choices=='C' or choices=='c':
			year ='2016'
			climbing_classes = [cclass for cclass in old_GWPC.FitnessClasses if "Climbing" in cclass["class"]]
			
			class_date_strs = [cclass['time'] for cclass in climbing_classes]

			class_dates = []
			for class_date_str in class_date_strs:
				#each class_date_str looks like 'Mar 30 @ 7:00 pm \xe2\x80\x93 8:15 pm'

				(date,_,rest) = class_date_str.partition(' @ ')

				#rest now looks like '7:00 pm \xe2\x80\x93 8:15 pm'


				from_time,_,to_time = rest.partition(' \xe2\x80\x93 ')

				#from_time now looks like '7:00 pm'
				#_ now looks like ' \xe2\x80\x93 '
				#to_time now looks like '8:15 pm'

				#from_time example: '2016 Mar 30 7:00 pm'
				from_date_time = year + ' ' + date + ' ' + from_time
				#to_time example: '2016 Mar 30 8:12 pm'
				to_date_time = year + ' ' + date + ' ' + to_time

				#from_date_time = from_date_time.replace('am', 'AM').replace('pm', 'PM')
				#to_date_time = to_date_time.replace('am', 'AM').replace('pm', 'PM')

				from_date_time = datetime.datetime.strptime(from_date_time, '%Y %b %d %I:%M %p')
				to_date_time = datetime.datetime.strptime(to_date_time, '%Y %b %d %I:%M %p')

				class_dates.append( (from_date_time, to_date_time) )

			print 'Select a time:-->'"\n\n"
			i = 1
			for (from_date_time,to_date_time) in class_dates:
				print ('%s.' % (i,) ), from_date_time.strftime('%b %d %I:%M %p'), '-', to_date_time.strftime('%b %d %I:%M %p')
				i += 1

			sys.stdout.flush()

			choices = raw_input()

			selection = int(choices) - 1

			(selection_date_from, selection_date_to) = class_dates[selection]

			print 'Climb on. Your Climbing clinic is from', selection_date_from.strftime('%b %d %I:%M %p'), '-', to_date_time.strftime('%b %d %I:%M %p')


	# elif choices=='Cr' or choices=='cr':
	# 		crossfit_classes = [crclass for crclass in old_GWPC.FitnessClasses if "Crossfit" in crclass["class"]]
	# 		print crossfit_classes
	# elif choices=='F' or choices=='f':
	# 		fitness_classes = [fclass for fclass in old_GWPC.FitnessClasses if "FitnessClasses" in fclass["class"]]
	# 		print fitness_classes
	else:
		print "Please enter (C) or (Y)"
		choice()
choice()
