import urllib2
import json
import re
from HTMLParser import HTMLParser


opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.open('https://touchstoneclimbing.time.ly/calendar/action~month/exact_date~1458100790/tag_ids~31,38/request_format~html/?callback=jQuery2001017656090995296836_1458100811092&request_type=jsonp&ai1ec_doing_ajax=true&_=1458100811094')
doc = response.read()
start = doc.find("{")
end = doc.find("}")
gwpc = doc[start:end + 1]

loc = json.loads(gwpc)

tree = loc["html"].encode("utf-8")
tree = tree.replace('&', '')

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.in_instructor = False
		self.in_class = False
		self.in_location = False
		self.in_time = False
		self.classNames = []
		self.eventTimes = []
		self.instructors = []
		self.locations = []
		self.last_tag = 0

	def handle_starttag(self, tag, attrs):
		# self.inLink = False
		self.in_instructor = False
		self.in_class = False
		self.in_location = False
		self.in_time = False
		if tag == 'a':
			for name, value in attrs:
				if name == 'class' and value == 'ai1ec-load-event':
					self.in_class = True
					self.last_tag = 0
		elif tag == 'div':
			for name, value in attrs:
				if name == 'class' and value == 'ai1ec-event-time':
					self.in_time = True
					self.last_tag = 1

	def handle_endtag(self, tag):
		if tag == "a" and self.last_tag == 0:
			self.in_class = False
		elif tag == "div" and self.last_tag == 1:
			self.in_time = False

	def handle_data(self, data):
		data = data.strip(' \t\n\r')
		if data:
			if self.in_class:
				self.classNames.append(data)
			elif self.in_time:
				self.eventTimes.append(data)


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

parser.feed(tree)

def getClasses(parser):
	result = []
	smallerIndex = min(len(parser.classNames), len(parser.eventTimes))

	for i in range(0, smallerIndex):
		new_class = {
			"class": parser.classNames[i],
			"time": parser.eventTimes[i]
		}
		result.append(new_class)

	return result

print getClasses(parser)




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
