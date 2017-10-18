from bs4 import BeautifulSoup
import unittest
import requests
import re

#########
## Instr note: the outline comments will stay as suggestions, otherwise it's too difficult.
## Of course, it could be structured in an easier/neater way, and if a student decides to commit to that, that is OK.

## NOTE OF ADVICE:
## When you go to make your GitHub milestones, think pretty seriously about all the different parts and their requirements, and what you need to understand. Make sure you've asked your questions about Part 2 as much as you need to before Fall Break!


######### PART 0 #########

# Write your code for Part 0 here.
try:
	gallery_data = open("gallery.html","r", encoding='utf-8').read()
except:
	gallery_data = requests.get("http://newmantaylor.com/gallery.html").text
	f = open("gallery.html","w",encoding = "utf-8")
	f.write(gallery_data)
	f.close

soup_gallery = BeautifulSoup(gallery_data, "html.parser")
# print (soup)

all_imgs = soup_gallery.find_all("img")
for i in all_imgs:
	print(i.get("alt","No alternative text provided!"))



######### PART 1 #########

try:
	nps_gov_data = open("nps_gov_data.html","r",encoding = "utf-8").read()
except:
	nps_gov_data = requests.get("https://www.nps.gov/index.htm").text
	f = open("nps_gov_data.html","w",encoding = "utf-8")
	f.write(nps_gov_data)
	f.close
 
home_page = "https://www.nps.gov"



# Get the main page data...

# Try to get and cache main page data if not yet cached
# Result of a following try/except block should be that
# there exists a file nps_gov_data.html,
# and the html text saved in it is stored in a variable 
# that the rest of the program can access.

# We've provided comments to guide you through the complex try/except, but if you prefer to build up the code to do this scraping and caching yourself, that is OK.

try:
	arkansas_data = open("arkansas_data.html","r",encoding = "utf-8").read()
	california_data = open("california_data.html","r",encoding = "utf-8").read()
	michigan_data = open("michigan_data.html","r",encoding ="utf-8").read()
except:
	soup_nps = BeautifulSoup(nps_gov_data,"html.parser")
	state_one = soup_nps.find("ul", class_ = "dropdown-menu")
	li_list = state_one.find_all("a")
	all_links = [x["href"] for x in li_list]
	pattern = re.compile(r'ar|ca|mi')
	specific_links = []
	for i in all_links:
		find = pattern.search(i)
		if find:
			specific_links.append(i)
	# print (home_page+specific_links[0])

	arkansas_data = requests.get(home_page + specific_links[0]).text
	f = open("arkansas_data.html","w",encoding = "utf-8")
	f.write(arkansas_data)
	f.close()
	california_data = requests.get(home_page + specific_links[1]).text
	f = open("california_data.html","w", encoding = "utf-8")
	f.write(california_data)
	f.close()
	michigan_data = requests.get(home_page + specific_links[2]).text
	f = open("michigan_data.html","w", encoding = "utf-8")
	f.write(michigan_data)
	f.close()



# Get individual states' data...

# Result of a following try/except block should be that
# there exist 3 files -- arkansas_data.html, california_data.html, michigan_data.html
# and the HTML-formatted text stored in each one is available
# in a variable or data structure 
# that the rest of the program can access.

# TRY: 
# To open and read all 3 of the files

# But if you can't, EXCEPT:

# Create a BeautifulSoup instance of main page data 
# Access the unordered list with the states' dropdown

# Get a list of all the li (list elements) from the unordered list, using the BeautifulSoup find_all method

# Use a list comprehension or accumulation to get all of the 'href' attributes of the 'a' tag objects in each li, instead of the full li objects

# Filter the list of relative URLs you just got to include only the 3 you want: AR's, CA's, MI's, using the accumulator pattern & conditional statements


# Create 3 URLs to access data from by appending those 3 href values to the main part of the NPS url. Save each URL in a variable.


## To figure out what URLs you want to get data from (as if you weren't told initially)...
# As seen if you debug on the actual site. e.g. Maine parks URL is "http://www.nps.gov/state/me/index.htm", Michigan's is "http://www.nps.gov/state/mi/index.htm" -- so if you compare that to the values in those href attributes you just got... how can you build the full URLs?


# Finally, get the HTML data from each of these URLs, and save it in the variables you used in the try clause
# (Make sure they're the same variables you used in the try clause! Otherwise, all this code will run every time you run the program!)


# And then, write each set of data to a file so this won't have to run again.







######### PART 2 #########


## Before truly embarking on Part 2, we recommend you do a few things:

# - Create BeautifulSoup objects out of all the data you have access to in variables from Part 1
# - Do some investigation on those BeautifulSoup objects. What data do you have about each state? How is it organized in HTML?

# HINT: remember the method .prettify() on a BeautifulSoup object -- might be useful for your investigation! So, of course, might be .find or .find_all, etc...

# HINT: Remember that the data you saved is data that includes ALL of the parks/sites/etc in a certain state, but you want the class to represent just ONE park/site/monument/lakeshore.

# We have provided, in sample_html_of_park.html an HTML file that represents the HTML about 1 park. However, your code should rely upon HTML data about Michigan, Arkansas, and Califoria you saved and accessed in Part 1.

# However, to begin your investigation and begin to plan your class definition, you may want to open this file and create a BeautifulSoup instance of it to do investigation on.

# Remember that there are things you'll have to be careful about listed in the instructions -- e.g. if no type of park/site/monument is listed in input, one of your instance variables should have a None value...

# soup_state = BeautifulSoup(arkansas_data,"html.parser")
# clearfix_one = soup_state.find("li",class_ = "clearfix")
# print (clearfix_one)
# Name = clearfix_one.find("a").text
# print (Name)
# location = clearfix_one.find("h4").text
# print (location)
# type_ = clearfix_one.find("h1231232")
# if not type_:
# 	type_ = 1
# print(type_)
# description = clearfix_one.find("p").text
# print(description.strip())
# li_list = clearfix_one.find_all("a")
# link = clearfix_one.find_all("a")[2]["href"]
# print(link)

# basic_info_data1 = requests.get(link).text
# basic_info_bs = BeautifulSoup(basic_info_data1,"html.parser")
# address = basic_info_bs.find("div",class_ = "physical-address")
# # print (address)
# streetAddress = address.find("span",itemprop = "streetAddress").text.strip()
# print (streetAddress)
# addressLocality = address.find("span",itemprop = "addressLocality")
# print (addressLocality.text)
# addressRegion = address.find("span",itemprop = "addressRegion")
# print (addressRegion.text)
# postalCode = address.find("span",itemprop = "postalCode")
# print (postalCode.text)
# # list1 = []
# # for x in span_items:
# # 	list1.append(x.text)
# # print (list1)



## Define your class NationalSite here:

class NationalSite(object):

	def __init__(self, nationalsite):
		self.nationalsite = nationalsite
		if nationalsite.find("h4"):
			self.location = nationalsite.find("h4").text
		else:
			self.location = None
		self.name = nationalsite.find("a").text
		if nationalsite.find("h2"):
			self.type = nationalsite.find("h2").text
		else:
			self.type = None
		if nationalsite.find("p"): 
			self.description =nationalsite.find("p").text.strip()
		else:
			self.description = ""

	def __str__(self):
		return "{} | {}".format(self.name,self.location)

	def get_mailing_address(self):
		if self.nationalsite:
			try:
				basic_info = open (self.name + ".html","r",encoding = "uft-8").read()
			except:
				basic_link = self.nationalsite.find_all("a")[2]["href"]
				basic_info = requests.get(basic_link).text
				f = open(self.name + ".html","w",encoding='utf-8')
				f.write(basic_info)
				f.close()

			basic_info_bs = BeautifulSoup(basic_info,"html.parser")
			if self.name != "Death Valley":
				if basic_info_bs.find("div",class_ = "mailing-address"):
					address = basic_info_bs.find("div",class_ = "mailing-address")
					if address.find("span",itemprop = "streetAddress"):
						streetAddress = address.find("span",itemprop = "streetAddress").text.strip()
					else:
						return None
					addressLocality = address.find("span",itemprop = "addressLocality").text.strip()
					addressRegion = address.find("span",itemprop = "addressRegion").text.strip()
					postalCode = address.find("span",itemprop = "postalCode").text.strip()
					return "{}\{}\{}\{}".format(streetAddress,addressLocality,addressRegion,postalCode)
				else:
					return ""
			else:
				address = basic_info_bs.find("div",class_ = "mailing-address")
				streetAddress = address.find("p",class_ ="adr").text.strip()[0:12]
				addressLocality = address.find("span",itemprop = "addressLocality").text.strip()
				addressRegion = address.find("span",itemprop = "addressRegion").text.strip()
				postalCode = address.find("span",itemprop = "postalCode").text.strip()
				return "{}\{}\{}\{}".format(streetAddress,addressLocality,addressRegion,postalCode)				

		else:
			return None

	def __contains__(self, park_name):
		result = park_name in self.name
		return result

	def return_for_csv(self):
		return '"{}","{}","{}","{}","{}"\n'.format(self.name,self.location,self.type,self.get_mailing_address(),self.description)




## Recommendation: to test the class, at various points, uncomment the following code and invoke some of the methods / check out the instance variables of the test instance saved in the variable sample_inst:

# f = open("sample_html_of_park.html",'r')
# soup_park_inst = BeautifulSoup(f.read(), 'html.parser') # an example of 1 BeautifulSoup instance to pass into your class
# sample_inst = NationalSite(soup_park_inst)
# print (str(sample_inst))
# f.close()


######### PART 3 #########


# soup_state = BeautifulSoup(arkansas_data,"html.parser")
# clearfix_one = soup_state.find_all("li",class_ = "clearfix")
# print (clearfix_one[1])

arkansas_natl_sites = []
california_natl_sites = []
michigan_natl_sites = []

arkansas_bs = BeautifulSoup(arkansas_data,"html.parser")
arkansas_li = arkansas_bs.find_all(lambda tag: tag.name == 'li' and tag.get('class') == ['clearfix'])
for item in arkansas_li:
	arkansas_natl_sites.append(NationalSite(item))


califoria_bs = BeautifulSoup(california_data,"html.parser")
california_li = califoria_bs.find_all(lambda tag: tag.name == 'li' and tag.get('class') == ['clearfix'])
for item in california_li:
	california_natl_sites.append(NationalSite(item))

michigan_bs = BeautifulSoup(michigan_data,"html.parser")
michigan_li = michigan_bs.find_all(lambda tag: tag.name == 'li' and tag.get('class') == ['clearfix'])
for item in michigan_li:
	michigan_natl_sites.append(NationalSite(item))

with open("arkansas.csv","w", encoding = "utf-8") as arkansas_file:
	arkansas_file.write('"Name","Location","Type","Address","Description"\n')
	for i in range (len(arkansas_natl_sites)):
		# print (arkansas_natl_sites[i])
		cont_str = arkansas_natl_sites[i].return_for_csv()
		# print (cont_str)
		arkansas_file.write(cont_str)

with open("california.csv","w",encoding = "utf-8") as california_file:
	california_file.write('"Name","Location","Type","Address","Description"\n')
	for i in range (len(california_natl_sites)):
		# print (arkansas_natl_sites[i])
		cont_str = california_natl_sites[i].return_for_csv()
		# print (cont_str)
		california_file.write(cont_str)

with open("michigan.csv","w", encoding = "utf-8") as michigan_file:
	michigan_file.write('"Name","Location","Type","Address","Description"\n')
	for i in range (len(michigan_natl_sites)):
		# print (arkansas_natl_sites[i])
		cont_str = michigan_natl_sites[i].return_for_csv()
		# print (cont_str)
		michigan_file.write(cont_str)





# Create lists of NationalSite objects for each state's parks.

# HINT: Get a Python list of all the HTML BeautifulSoup instances that represent each park, for each state.




##Code to help you test these out:
# for p in california_natl_sites:
# 	print(p)
# for a in arkansas_natl_sites:
# 	print(a)
# for m in michigan_natl_sites:
# 	print(m)



######### PART 4 #########

## Remember the hints / things you learned from Project 2 about writing CSV files from lists of objects!

## Note that running this step for ALL your data make take a minute or few to run -- so it's a good idea to test any methods/functions you write with just a little bit of data, so running the program will take less time!

## Also remember that IF you have None values that may occur, you might run into some problems and have to debug for where you need to put in some None value / error handling!

