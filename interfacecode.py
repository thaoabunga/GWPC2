import old_GWPC
import datetime


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
print 'What are you interested in today?'"\n\n"

def choice():
	choices =raw_input("(C)limbing , (Cr)ossFit , or (Y)oga?")
	if choices=='Y' or choices=='y':
			yoga_classes = [yclass for yclass in old_GWPC.FitnessClasses if "Yoga" in yclass["class"]]
			# newlist = []
			# newlist = sorted(yoga_classes, key=lambda k: k['time']) 
			# s = 'Mar 10 @ 7:30 am'
			# ask user what time?
			# format = '%Y-%m-%d %H:%M:'
			# date=datetime.datetime.strptime(s, format)
			# date
			# datetime.datetime(2016, 3)

			print yoga_classes
			#change yoga classes into data objects
			#sort yoga classes by date
			#print yoga classes by date
	elif choices=='C' or choices=='c':
			climbing_classes = [cclass for cclass in old_GWPC.FitnessClasses if "Climbing" in cclass["class"]]
			print climbing_classes
	# elif choices=='Cr' or choices=='cr':
	# 		crossfit_classes = [crclass for crclass in old_GWPC.FitnessClasses if "Crossfit" in crclass["class"]]
	# 		print crossfit_classes
	# elif choices=='F' or choices=='f':
	# 		fitness_classes = [fclass for fclass in old_GWPC.FitnessClasses if "FitnessClasses" in fclass["class"]]
	# 		print fitness_classes
	else: 
		print "Try again"
		choice()

choice()
