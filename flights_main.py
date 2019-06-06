import flights
import pandas as pd
from pandas import ExcelWriter
uk_list = ['Greater London, London',
 'Buckinghamshire, London',
 'Cambridgeshire, London',
 'Durham, London',
 'East Riding of Yorkshire, London',
 'East Sussex , London',
 'Essex, London',
 'Gloucestershire, London',
 'Greater Manchester, London',
 'Halton, London',
 'Hampshire, London',
 'Hartlepool, London',
 'Herefordshire, London',
 'Oxfordshire, London',
 'Rutland, London',
 'Shropshire, London',
 'Slough, London',
 'Somerset, London']

canada_list =  ['Alberta, Canada',
 'British Columbia, Canada',
 'Canada, Canada',
 'Manitoba, Canada',
 'New Brunswick, Canada',
 'Newfoundland and Labrador, Canada',
 'Nova Scotia, Canada',
 'Ontario, Canada',
 'Prince Edward Island, Canada',
 'Quebec, Canada',
 'Saskatchewan, Canada',
 'Yukon , Canada']

america_list=["Oak Bluffs, MA",
	"Orlando, FL",
	"New York, NY",
	"Durham, NC",
	"Green Bay, WI",
	"Atlantic City, New Jersey"]
date_list = ["2019-08-30", "2019-09-10", "2019-09-20", "2019-09-30", "2019-10-09", "2019-10-19", "2019-10-29", "2019-11-08", "2019-11-18"]
# flight = flights.CheapFlights("Richmond", "Alberta, Canada" , "2019-09-20", "2020-02-20")
# print(flight.get_cheapest())

price_list = []
city_list = []
number_days_out_list = [] 
for i in range(len(america_list)):
	for x in range(len(date_list)):
		try:
			flight = flights.CheapFlights("Richmond", america_list[i] , "2019-08-20", date_list[x])
			cheap_price = flight.get_cheapest()
			days = (x + 1) * 10
			print(cheap_price)
			city_list.append(america_list[i])
			price_list.append(cheap_price)
			number_days_out_list.append(days)
		except:
			continue

df = pd.DataFrame(
    {'City': city_list,
     'Days Out': number_days_out_list,
     'Price': price_list
    })

writer = pd.ExcelWriter('america_list.xlsx')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()






	    