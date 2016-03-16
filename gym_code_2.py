import urllib2
import json
from HTMLParser import HTMLParser

from GWPC import MyHTMLParser
print "second line"
# instantiate the parser and fed it some HTML
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.open('https://touchstoneclimbing.time.ly/calendar/action~month/exact_date~1456819200/tag_ids~35/request_format~html/?ai1ec_source=ai1ec_superwidget&ai1ec_source=ai1ec_superwidget&callback=jQuery20010734922839794308_1457318427869&request_type=jsonp&ai1ec_doing_ajax=true&_=1457318427871')
doc = response.read()
start = doc.find("{")
end = doc.find("}")
gwpc = doc[start:end + 1]
loc = json.loads(gwpc)

tree = loc["html"].encode('utf-8')

parser = MyHTMLParser()

parser.feed(tree)

data =  parser.returned_data
data = data.replace("\t","")
data = data.replace("\n\n\n","")
data = data.split("@ Great Western Power Company")
print data[7]
print data[7].split("Instructor:")[1].split("\n")[0]
print "last line"
# greets person, asks him or her which fitness class they're interested in
# def greet(name):
# 	return "Hello " + name

# def chooseFitnessExp(numberOfExps):
# 	choice = raw_input(">")
# 	while choice < 1 or choice > numberOfExps: 
# 		if choice != 'Climbing_Clinics' and choice != 'CrossFit' and choice != 'Fitness_Classes' and choice != 'Fitness_Clinics'  and choice != 'Indoor_Cycling' and choice != 'Yoga' and choice != 'Yoga_Clinics':
# 			choice = 0
# 	if choice == 'Climbing_Clinics' or choice == 'CrossFit' or choice == 'Fitness_Classes' or choice == 'Fitness_Clinics' or choice == 'Indoor_Cycling' or choice == 'Yoga' or choice == 'Yoga_Clinics':
# 		choice = int(choice)
# 	print()
# 	return choice


# # greeting_someone = greet

# print greeting_someone("Athena! Which fitness class are you interested in?")
# choice = chooseFitnessExp()