import urllib2
import json
from HTMLParser import HTMLParser


opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.open('https://touchstoneclimbing.time.ly/calendar/action~month/exact_date~1456819200/tag_ids~35/request_format~html/?ai1ec_source=ai1ec_superwidget&ai1ec_source=ai1ec_superwidget&callback=jQuery20010734922839794308_1457318427869&request_type=jsonp&ai1ec_doing_ajax=true&_=1457318427871')
doc = response.read()
start = doc.find("{")
end = doc.find("}")
gwpc = doc[start:end + 1]
loc = json.loads(gwpc)

tree = loc["html"].encode('utf-8')

# print tree

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.in_div = False
		self.in_span = False
		self.dataArray = []
		self.countLanguages = 0
		self.lasttag = None
		self.lastname = None
		self.lastvalue = None

	def handle_starttag(self, tag, attrs):
		# self.inLink = False
		if tag == 'div':
			self.in_div = True
		elif tag == 'span':
			if self.in_div:
				for name, value in attrs:
					# print name
					# print value
					if name == 'class' and value == 'ai1ec-event-title':
						self.in_span = True
					if name == 'class' and value == 'ai1ec-event-time':
						self.in_span = True

	def handle_endtag(self, tag):
		if tag == "div":
			self.in_div = True
		if tag == "span":
			self.in_span = True

	def handle_data(self, data):
		if self.in_span:
			print data
			# print ""

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

parser.feed(tree)



# print tree

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
