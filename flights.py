from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import pandas as pd
import time
import datetime

return_ticket = "//label[@id='flight-type-roundtrip-label-hp-flight']"
one_way_ticket = "//label[@id='flight-type-one-way-label-hp-flight']"
multi_ticket = "//label[@id='flight-type-multi-dest-label-hp-flight']"

class CheapFlights:
	def __init__(self, departure_city, arrival_city, departure_date, arrival_date):
		self.departure_city = departure_city
		self.arrival_city = arrival_city
		self.departure_date = departure_date
		self.arrival_date = arrival_date	
		self.browser = webdriver.Chrome(executable_path='/Users/markkang/Downloads/chromedriver')

	def ticket_chooser(self,ticket):
	    try:
	        ticket_type = self.browser.find_element_by_xpath(ticket)
	        ticket_type.click()
	    except Exception as e:
	        pass

	def dep_country_chooser(self, dep_country):
	    fly_from = self.browser.find_element_by_xpath("//input[@id='flight-origin-hp-flight']")
	    time.sleep(1)
	    fly_from.clear()
	    time.sleep(0.5)
	    fly_from.send_keys('  ' + dep_country)
	    time.sleep(1.5)
	    first_item = self.browser.find_element_by_xpath("//a[@id='aria-option-0']")
	    time.sleep(1.5)
	    first_item.click()

	def arrival_country_chooser(self, arrival_country):
	    fly_to = self.browser.find_element_by_xpath("//input[@id='flight-destination-hp-flight']")
	    time.sleep(1)
	    fly_to.clear()
	    time.sleep(0.5)
	    fly_to.send_keys('  ' + arrival_country)
	    time.sleep(1.5)
	    first_item = self.browser.find_element_by_xpath("//a[@id='aria-option-0']")
	    time.sleep(1.5)
	    first_item.click()

	def dep_date_chooser(self, month, day, year):
	    dep_date_button = self.browser.find_element_by_xpath("//input[@id='flight-departing-hp-flight']")
	    dep_date_button.clear()
	    dep_date_button.send_keys(month + '/' + day + '/' + year)

	def return_date_chooser(self, month, day, year):
	    return_date_button = self.browser.find_element_by_xpath("//input[@id='flight-returning-hp-flight']")
	    for i in range(11):
	        return_date_button.send_keys(Keys.BACKSPACE)
	    return_date_button.send_keys(month + '/' + day + '/' + year)

	def search(self):
	    search = self.browser.find_element_by_xpath("//button[@class='btn-primary btn-action gcw-submit']")
	    search.click()
	    print('Results ready!')


	def compile_data(self):
	    global df
	    global dep_times_list
	    global arr_times_list
	    global airlines_list
	    global price_list
	    global durations_list
	    global stops_list
	    global layovers_list
	    df = pd.DataFrame()
	    #departure times
	    dep_times = self.browser.find_elements_by_xpath("//span[@data-test-id='departure-time']")
	    dep_times_list = [value.text for value in dep_times]
	    #arrival times
	    arr_times = self.browser.find_elements_by_xpath("//span[@data-test-id='arrival-time']")
	    arr_times_list = [value.text for value in arr_times]
	    #airline name
	    airlines = self.browser.find_elements_by_xpath("//span[@data-test-id='airline-name']")
	    airlines_list = [value.text for value in airlines]
	    #prices
	    prices = self.browser.find_elements_by_xpath("//span[@data-test-id='listing-price-dollars']")
	    price_list = [value.text for value in prices]
	    #durations
	    durations = self.browser.find_elements_by_xpath("//span[@data-test-id='duration']")
	    durations_list = [value.text for value in durations]
	    #stops
	    stops = self.browser.find_elements_by_xpath("//span[@class='number-stops']")
	    stops_list = [value.text for value in stops]
	    #layovers
	    layovers = self.browser.find_elements_by_xpath("//span[@data-test-id='layover-airport-stops']")
	    layovers_list = [value.text for value in layovers]
	    now = datetime.datetime.now()
	    current_date = (str(now.year) + '-' + str(now.month) + '-' + str(now.day))
	    current_time = (str(now.hour) + ':' + str(now.minute))
	    current_price = 'price' + '(' + current_date + '---' + current_time + ')'
	    for i in range(len(dep_times_list)):
	        try:
	            df.loc[i, 'departure_time'] = dep_times_list[i]
	        except Exception as e:
	            pass
	        try:
	            df.loc[i, 'arrival_time'] = arr_times_list[i]
	        except Exception as e:
	            pass
	        try:
	            df.loc[i, 'airline'] = airlines_list[i]
	        except Exception as e:
	            pass
	        try:
	            df.loc[i, 'duration'] = durations_list[i]
	        except Exception as e:
	            pass
	        try:
	            df.loc[i, 'stops'] = stops_list[i]
	        except Exception as e:
	            pass
	        try:
	            df.loc[i, 'layovers'] = layovers_list[i]
	        except Exception as e:
	            pass
	        try:
	            df.loc[i, str(current_price)] = price_list[i]
	        except Exception as e:
	            pass
	def get_cheapest(self):
		#save values for email
		# cheapest_dep_time = current_values[0] 
		# cheapest_arrival_time = current_values[1]
		# cheapest_airline = current_values[2]
		# cheapest_duration = current_values[3]
		# cheapest_stops = current_values[4]
		link = 'https://www.expedia.com/'
		# browser = webdriver.Chrome(executable_path='/Users/markkang/Downloads/chromedriver')
		self.browser.get(link)
		time.sleep(4)
		#choose flights only
		flights_only = self.browser.find_element_by_xpath("//button[@id='tab-flight-tab-hp']")
		flights_only.click()
		self.ticket_chooser(return_ticket)
		self.dep_country_chooser(self.departure_city)
		self.arrival_country_chooser(self.arrival_city)
		dep_date_list = self.date_parser(self.departure_date)
		arr_date_list = self.date_parser(self.arrival_date)
		self.dep_date_chooser(dep_date_list[1], dep_date_list[2], dep_date_list[0])
		self.return_date_chooser(arr_date_list[1], arr_date_list[2], arr_date_list[0])
		self.search()
		time.sleep(15)
		self.compile_data()
		time.sleep(9)
		current_values = df.iloc[0]
		cheapest_price = current_values[-1]
		self.browser.close()
		return cheapest_price

	def date_parser(self,date):
		date_list = date.split("-")
		return date_list  

