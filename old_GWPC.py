# import urllib2
# import json
# import re
# from HTMLParser import HTMLParser


# opener = urllib2.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# response = opener.open('https://touchstoneclimbing.time.ly/calendar/action~month/exact_date~1458100790/tag_ids~31,38/request_format~html/?callback=jQuery2001017656090995296836_1458100811092&request_type=jsonp&ai1ec_doing_ajax=true&_=1458100811094')
# doc = response.read()
# start = doc.find("{")
# end = doc.find("}")
# gwpc = doc[start:end + 1]

# loc = json.loads(gwpc)

# tree = loc["html"].encode("utf-8")
# tree = tree.replace('&', '')

# # create a subclass and override the handler methods
# class MyHTMLParser(HTMLParser):
# 	def __init__(self):
# 		HTMLParser.__init__(self)
# 		self.in_instructor = False
# 		self.in_class = False
# 		self.in_location = False
# 		self.in_time = False
# 		self.classNames = []
# 		self.eventTimes = []
# 		self.instructors = []
# 		self.locations = []
# 		self.last_tag = 0

# 	def handle_starttag(self, tag, attrs):
# 		# self.inLink = False
# 		self.in_instructor = False
# 		self.in_class = False
# 		self.in_location = False
# 		self.in_time = False
# 		if tag == 'a':
# 			for name, value in attrs:
# 				if name == 'class' and value == 'ai1ec-load-event':
# 					self.in_class = True
# 					self.last_tag = 0
# 		elif tag == 'div':
# 			for name, value in attrs:
# 				if name == 'class' and value == 'ai1ec-event-time':
# 					self.in_time = True
# 					self.last_tag = 1

# 	def handle_endtag(self, tag):
# 		if tag == "a" and self.last_tag == 0:
# 			self.in_class = False
# 		elif tag == "div" and self.last_tag == 1:
# 			self.in_time = False

# 	def handle_data(self, data):
# 		data = data.strip(' \t\n\r')
# 		if data:
# 			if self.in_class:
# 				self.classNames.append(data)
# 			elif self.in_time:
# 				self.eventTimes.append(data)


# # instantiate the parser and fed it some HTML
# parser = MyHTMLParser()

# parser.feed(tree)

# def getClasses(parser):
# 	result = []
# 	smallerIndex = min(len(parser.classNames), len(parser.eventTimes))

# 	for i in range(0, smallerIndex):
# 		new_class = {
# 			"class": parser.classNames[i],
# 			"time": parser.eventTimes[i]
# 		}
# 		result.append(new_class)

# 	return result

# print getClasses(parser)

# loc position value and corresponding index

for i, v in enumerate([{'class': 'Indoor Cycling', 'time': 'Mar 1 @ 7:00 am \xe2\x80\x93 8:00 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 1 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa Flow', 'time': 'Mar 1 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Strength', 'time': 'Mar 1 @ 11:00 am \xe2\x80\x93 12:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 1 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 1 @ 4:30 pm \xe2\x80\x93 5:25 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 1 @ 5:30 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 1 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Beta Bouldering', 'time': 'Mar 1 @ 6:30 pm \xe2\x80\x93 7:30 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 1 @ 7:00 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Cardio Boxing', 'time': 'Mar 1 @ 8:20 pm \xe2\x80\x93 9:35 pm'}, {'class': 'Sparring', 'time': 'Mar 1 @ 9:45 pm \xe2\x80\x93 10:45 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 2 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 2 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 2 @ 6:00 pm \xe2\x80\x93 7:15 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 2 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Massage by Body Awakening', 'time': 'Mar 2 @ 6:00 pm \xe2\x80\x93 9:00 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 2 @ 7:00 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 3 @ 7:00 am \xe2\x80\x93 8:00 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 3 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 3 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Flow', 'time': 'Mar 3 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Strength', 'time': 'Mar 3 @ 11:00 am \xe2\x80\x93 12:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 3 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Therapeutic Yoga', 'time': 'Mar 3 @ 4:15 pm \xe2\x80\x93 5:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 3 @ 5:30 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 3 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Acro Yoga', 'time': 'Mar 3 @ 6:45 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 3 @ 7:00 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Cardio Boxing', 'time': 'Mar 3 @ 8:20 pm \xe2\x80\x93 9:35 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 4 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa Flow', 'time': 'Mar 4 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 4 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Yoga: Ashtanga', 'time': 'Mar 4 @ 5:45 pm \xe2\x80\x93 7:00 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 4 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Yoga: Slow-Flow', 'time': 'Mar 4 @ 7:15 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Yoga: Hatha', 'time': 'Mar 5 @ 9:30 am \xe2\x80\x93 10:30 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 5 @ 11:00 am \xe2\x80\x93 12:30 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 5 @ 2:30 pm \xe2\x80\x93 3:00 pm'}, {'class': 'Core the Yoga Way', 'time': 'Mar 6 @ 9:30 am \xe2\x80\x93 10:30 am'}, {'class': 'Yoga: Flow', 'time': 'Mar 6 @ 11:00 am \xe2\x80\x93 12:30 pm'}, {'class': 'Yoga: Flight School', 'time': 'Mar 6 @ 1:00 pm \xe2\x80\x93 2:15 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 6 @ 2:30 pm \xe2\x80\x93 3:00 pm'}, {'class': 'Beyond Belay', 'time': 'Mar 6 @ 6:30 pm \xe2\x80\x93 7:30 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 7 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga:  Rocket Yoga', 'time': 'Mar 7 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 7 @ 6:00 pm \xe2\x80\x93 7:15 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 7 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Beyond Belay', 'time': 'Mar 7 @ 6:30 pm \xe2\x80\x93 7:30 pm'}, {'class': 'Massage Night', 'time': 'Mar 7 @ 7:00 pm \xe2\x80\x93 10:00 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 7 @ 7:00 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Yoga: Yin', 'time': 'Mar 7 @ 8:30 pm \xe2\x80\x93 9:45 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 8 @ 7:00 am \xe2\x80\x93 8:00 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 8 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa Flow', 'time': 'Mar 8 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Strength', 'time': 'Mar 8 @ 11:00 am \xe2\x80\x93 12:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 8 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 8 @ 4:30 pm \xe2\x80\x93 5:25 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 8 @ 5:30 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 8 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Beta Bouldering', 'time': 'Mar 8 @ 6:30 pm \xe2\x80\x93 7:30 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 8 @ 7:00 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Cardio Boxing', 'time': 'Mar 8 @ 8:20 pm \xe2\x80\x93 9:35 pm'}, {'class': 'Sparring', 'time': 'Mar 8 @ 9:45 pm \xe2\x80\x93 10:45 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 9 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 9 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 9 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 9 @ 6:00 pm \xe2\x80\x93 7:15 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 9 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 9 @ 7:00 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 10 @ 7:00 am \xe2\x80\x93 8:00 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 10 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 10 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Flow', 'time': 'Mar 10 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Strength', 'time': 'Mar 10 @ 11:00 am \xe2\x80\x93 12:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 10 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Therapeutic Yoga', 'time': 'Mar 10 @ 4:15 pm \xe2\x80\x93 5:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 10 @ 5:30 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 10 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Shoe Demo', 'time': 'Mar 10 @ 6:00 pm \xe2\x80\x93 9:00 pm'}, {'class': 'Acro Yoga', 'time': 'Mar 10 @ 6:45 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 10 @ 7:00 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Cardio Boxing', 'time': 'Mar 10 @ 8:20 pm \xe2\x80\x93 9:35 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 11 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa Flow', 'time': 'Mar 11 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 11 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Yoga: Ashtanga', 'time': 'Mar 11 @ 5:45 pm \xe2\x80\x93 7:00 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 11 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Yoga: Slow-Flow', 'time': 'Mar 11 @ 7:15 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Yoga: Hatha', 'time': 'Mar 12 @ 9:30 am \xe2\x80\x93 10:30 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 12 @ 11:00 am \xe2\x80\x93 12:30 pm'}, {'class': 'Arm Balance Workshop with Maria', 'time': 'Mar 12 @ 2:30 pm \xe2\x80\x93 4:30 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 12 @ 2:30 pm \xe2\x80\x93 3:00 pm'}, {'class': 'Lead 1', 'time': 'Mar 12 @ 6:00 pm \xe2\x80\x93 8:00 pm'}, {'class': 'Core the Yoga Way', 'time': 'Mar 13 @ 9:30 am \xe2\x80\x93 10:30 am'}, {'class': 'Yoga: Flow', 'time': 'Mar 13 @ 11:00 am \xe2\x80\x93 12:30 pm'}, {'class': 'Yoga: Flight School', 'time': 'Mar 13 @ 1:00 pm \xe2\x80\x93 2:15 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 13 @ 2:30 pm \xe2\x80\x93 3:00 pm'}, {'class': 'Basic Technique', 'time': 'Mar 13 @ 5:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Lead 2', 'time': 'Mar 13 @ 6:00 pm \xe2\x80\x93 8:00 pm'}, {'class': 'Beyond Belay', 'time': 'Mar 13 @ 6:30 pm \xe2\x80\x93 7:30 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 14 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga:  Rocket Yoga', 'time': 'Mar 14 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Yoga:  Rocket Yoga', 'time': 'Mar 14 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 14 @ 6:00 pm \xe2\x80\x93 7:15 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 14 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Beyond Belay', 'time': 'Mar 14 @ 6:30 pm \xe2\x80\x93 7:30 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 14 @ 7:00 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Yoga: Yin', 'time': 'Mar 14 @ 8:30 pm \xe2\x80\x93 9:45 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 15 @ 7:00 am \xe2\x80\x93 8:00 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 15 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa Flow', 'time': 'Mar 15 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Strength', 'time': 'Mar 15 @ 11:00 am \xe2\x80\x93 12:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 15 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 15 @ 4:30 pm \xe2\x80\x93 5:25 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 15 @ 5:30 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 15 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 15 @ 7:00 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Cardio Boxing', 'time': 'Mar 15 @ 8:20 pm \xe2\x80\x93 9:35 pm'}, {'class': 'Sparring', 'time': 'Mar 15 @ 9:45 pm \xe2\x80\x93 10:45 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 16 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 16 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 16 @ 6:00 pm \xe2\x80\x93 7:15 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 16 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Shoe Demo', 'time': 'Mar 16 @ 6:00 pm \xe2\x80\x93 9:00 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 16 @ 7:00 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 17 @ 7:00 am \xe2\x80\x93 8:00 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 17 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 17 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Flow', 'time': 'Mar 17 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Strength', 'time': 'Mar 17 @ 11:00 am \xe2\x80\x93 12:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 17 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Therapeutic Yoga', 'time': 'Mar 17 @ 4:15 pm \xe2\x80\x93 5:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 17 @ 5:30 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Friction Labs Chalk Demo', 'time': 'Mar 17 @ 6:00 pm \xe2\x80\x93 8:00 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 17 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Acro Yoga', 'time': 'Mar 17 @ 6:45 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 17 @ 7:00 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Cardio Boxing', 'time': 'Mar 17 @ 8:20 pm \xe2\x80\x93 9:35 pm'}, {'class': 'College Student Night', 'time': 'Mar 18'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 18 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa Flow', 'time': 'Mar 18 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 18 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Touchstone Climbing Series: Ropes', 'time': 'Mar 18 @ 5:00 pm \xe2\x80\x93 10:00 pm'}, {'class': 'Yoga: Ashtanga', 'time': 'Mar 18 @ 5:45 pm \xe2\x80\x93 7:00 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 18 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Yoga: Slow-Flow', 'time': 'Mar 18 @ 7:15 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Yoga: Hatha', 'time': 'Mar 19 @ 9:30 am \xe2\x80\x93 10:30 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 19 @ 11:00 am \xe2\x80\x93 12:30 pm'}, {'class': 'Yoga Beyond the Asanas: Part 1 with Sam', 'time': 'Mar 19 @ 1:30 pm \xe2\x80\x93 3:00 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 19 @ 2:30 pm \xe2\x80\x93 3:00 pm'}, {'class': 'Lead 1', 'time': 'Mar 19 @ 6:00 pm \xe2\x80\x93 8:00 pm'}, {'class': 'Core the Yoga Way', 'time': 'Mar 20 @ 9:30 am \xe2\x80\x93 10:30 am'}, {'class': 'Yoga: Flow', 'time': 'Mar 20 @ 11:00 am \xe2\x80\x93 12:30 pm'}, {'class': 'Yoga: Flight School', 'time': 'Mar 20 @ 1:00 pm \xe2\x80\x93 2:15 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 20 @ 2:30 pm \xe2\x80\x93 3:00 pm'}, {'class': 'Boxing Booster Class w/ Victor amp; Harmony', 'time': 'Mar 20 @ 4:00 pm \xe2\x80\x93 6:00 pm'}, {'class': 'Basic Technique', 'time': 'Mar 20 @ 6:00 pm \xe2\x80\x93 7:30 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 21 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga:  Rocket Yoga', 'time': 'Mar 21 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 21 @ 6:00 pm \xe2\x80\x93 7:15 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 21 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Beyond Belay', 'time': 'Mar 21 @ 6:30 pm \xe2\x80\x93 7:30 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 21 @ 7:00 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Beta Bouldering', 'time': 'Mar 21 @ 7:30 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Yoga: Yin', 'time': 'Mar 21 @ 8:30 pm \xe2\x80\x93 9:45 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 22 @ 7:00 am \xe2\x80\x93 8:00 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 22 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa Flow', 'time': 'Mar 22 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Strength', 'time': 'Mar 22 @ 11:00 am \xe2\x80\x93 12:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 22 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 22 @ 4:30 pm \xe2\x80\x93 5:25 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 22 @ 5:30 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 22 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 22 @ 7:00 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Cardio Boxing', 'time': 'Mar 22 @ 8:20 pm \xe2\x80\x93 9:35 pm'}, {'class': 'Sparring', 'time': 'Mar 22 @ 9:45 pm \xe2\x80\x93 10:45 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 23 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 23 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 23 @ 6:00 pm \xe2\x80\x93 7:15 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 23 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 23 @ 7:00 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 24 @ 7:00 am \xe2\x80\x93 8:00 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 24 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 24 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Flow', 'time': 'Mar 24 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Strength', 'time': 'Mar 24 @ 11:00 am \xe2\x80\x93 12:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 24 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Therapeutic Yoga', 'time': 'Mar 24 @ 4:15 pm \xe2\x80\x93 5:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 24 @ 5:30 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 24 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Beyond Belay', 'time': 'Mar 24 @ 6:30 pm \xe2\x80\x93 7:30 pm'}, {'class': 'Acro Yoga', 'time': 'Mar 24 @ 6:45 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 24 @ 7:00 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Cardio Boxing', 'time': 'Mar 24 @ 8:20 pm \xe2\x80\x93 9:35 pm'}, {'class': 'Free Member Guest Day', 'time': 'Mar 25'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 25 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa Flow', 'time': 'Mar 25 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 25 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Yoga: Ashtanga', 'time': 'Mar 25 @ 5:45 pm \xe2\x80\x93 7:00 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 25 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Yoga: Slow-Flow', 'time': 'Mar 25 @ 7:15 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Yoga: Hatha', 'time': 'Mar 26 @ 9:30 am \xe2\x80\x93 10:30 am'}, {'class': 'Slab Climbing', 'time': 'Mar 26 @ 10:30 am \xe2\x80\x93 12:00 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 26 @ 11:00 am \xe2\x80\x93 12:30 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 26 @ 2:30 pm \xe2\x80\x93 3:00 pm'}, {'class': 'Lead 1', 'time': 'Mar 26 @ 6:00 pm \xe2\x80\x93 8:00 pm'}, {'class': 'Core the Yoga Way', 'time': 'Mar 27 @ 9:30 am \xe2\x80\x93 10:30 am'}, {'class': 'Yoga: Flow', 'time': 'Mar 27 @ 11:00 am \xe2\x80\x93 12:30 pm'}, {'class': 'Yoga: Flight School', 'time': 'Mar 27 @ 1:00 pm \xe2\x80\x93 2:15 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 27 @ 2:30 pm \xe2\x80\x93 3:00 pm'}, {'class': 'Intermediate Technique', 'time': 'Mar 27 @ 4:00 pm \xe2\x80\x93 6:00 pm'}, {'class': 'Basic Technique', 'time': 'Mar 27 @ 6:00 pm \xe2\x80\x93 7:30 pm'}, {'class': 'Lead 2', 'time': 'Mar 27 @ 6:00 pm \xe2\x80\x93 8:00 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 28 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga:  Rocket Yoga', 'time': 'Mar 28 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 28 @ 6:00 pm \xe2\x80\x93 7:15 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 28 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Beyond Belay', 'time': 'Mar 28 @ 6:30 pm \xe2\x80\x93 7:30 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 28 @ 7:00 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Beta Bouldering', 'time': 'Mar 28 @ 7:30 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Yoga: Yin', 'time': 'Mar 28 @ 8:30 pm \xe2\x80\x93 9:45 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 29 @ 7:00 am \xe2\x80\x93 8:00 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 29 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa Flow', 'time': 'Mar 29 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Strength', 'time': 'Mar 29 @ 11:00 am \xe2\x80\x93 12:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 29 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 29 @ 4:30 pm \xe2\x80\x93 5:25 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 29 @ 5:30 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 29 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 29 @ 7:00 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Cardio Boxing', 'time': 'Mar 29 @ 8:20 pm \xe2\x80\x93 9:35 pm'}, {'class': 'Sparring', 'time': 'Mar 29 @ 9:45 pm \xe2\x80\x93 10:45 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 30 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 30 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 30 @ 6:00 pm \xe2\x80\x93 7:15 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 30 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 30 @ 7:00 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 31 @ 7:00 am \xe2\x80\x93 8:00 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 31 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 31 @ 7:30 am \xe2\x80\x93 8:30 am'}, {'class': 'Yoga: Flow', 'time': 'Mar 31 @ 8:45 am \xe2\x80\x93 9:45 am'}, {'class': 'Strength', 'time': 'Mar 31 @ 11:00 am \xe2\x80\x93 12:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 31 @ 12:00 pm \xe2\x80\x93 1:00 pm'}, {'class': 'Therapeutic Yoga', 'time': 'Mar 31 @ 4:15 pm \xe2\x80\x93 5:15 pm'}, {'class': 'Yoga: Vinyasa', 'time': 'Mar 31 @ 5:30 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Girl Beta', 'time': 'Mar 31 @ 6:00 pm \xe2\x80\x93 7:00 pm'}, {'class': 'Intro to Bouldering', 'time': 'Mar 31 @ 6:00 pm \xe2\x80\x93 6:30 pm'}, {'class': 'Beyond Belay', 'time': 'Mar 31 @ 6:30 pm \xe2\x80\x93 7:30 pm'}, {'class': 'Acro Yoga', 'time': 'Mar 31 @ 6:45 pm \xe2\x80\x93 8:15 pm'}, {'class': 'Indoor Cycling', 'time': 'Mar 31 @ 7:00 pm \xe2\x80\x93 8:30 pm'}, {'class': 'Cardio Boxing', 'time': 'Mar 31 @ 8:20 pm \xe2\x80\x93 9:35 pm'}]):

	print i,v






# from lxml import html
# import requests 

# requestURL = 'https://touchstoneclimbing.com/gwpower-co/calendar/'

# page = requests.get(requestURL)
# tree = html.fromstring(page.text)
																					
# calendar = tree.xpath('//table[@class="ai1ec-month-view"]/text()')

# print calendar

# for athena in tree:
# 	print athena


# print len(tree)

#for name, value in attrs:
            			# if name == 'mode':
                		# value = 0
                		
                		# # print(value)
                		# self.countLanguages += 1
                		# self.inLink = True

                		#self.lasttag = 'div'
