# import old_GWPC

print "+++Great Western Power Company's Fitness Calendar+++""\n"
print "|Climbing | CrossFit | Fitness Classes | Yoga |""\n"

import time;
localtime = time.asctime( time.localtime(time.time()) )

print "Today is", localtime 

import calendar

cal = calendar.month(2016, 3) 
print "--------------------------""\n"
print cal

#the available classes for today are
#find a way to list classes for the date
print 'What are you interested in today?'"\n"

def choice():
	choices =raw_input("(C)limbing , (Cr)ossFit , (F)itness Classes , or (Y)oga?")
	if choices=='Y' or choices=='y':
			
			print "x"
	elif choices=='C' or choices=='c':
			print "climb on"
	elif choices=='F' or choices=='f':
			print "hello"
	elif choices=='Cr' or choices=='cr':
			print "bye"
	else: 
			print "Try again"
			choice()
choice()
