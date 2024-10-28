# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import requests

states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
    "New Hampshire", "New Jersey", "New Mexico", "New York",
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
    "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
headers = {
		"x-rapidapi-key": "4231a7803amshdfe0e50e656c063p1cedc2jsnd94622b83e0f",
		"x-rapidapi-host": "covid-19-statistics.p.rapidapi.com"
	}

with open('01_to_06_2022_V2.csv', mode='w') as csvfile:
	fieldnames = ['date', 'last_update', 'confirmed', 'confirmed_diff', 'deaths', 'deaths_diff', 'recovered',
				  'recovered_diff', 'active', 'active_diff', 'fatality_rate', 'state',]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

# for x in states:
	# Define the day as a variable

	# Change this to whatever day you want
	for x in states:
		print(x)

	for x in states:
		i = 1
		month_variable = "01"
		while i <= 6:
			j = 1
			day_variable= "01"
			while j < 32:
				# Combine the fixed "2022-04" with the variable day
				date_variable = str(f"2022-{month_variable}-{day_variable}")
				print(date_variable)

				# Use the date_variable in the querystring
				querystring = {
					"iso": "USA",
					"region_province": x,
					"region_name": "US",
					"date": date_variable  # Using the variable here
				}

				#Requesting data
				response = requests.get(url, headers=headers, params=querystring)
				myDict = response.json().get("data")
				print(type(myDict))
				# ctrl / to comment out



				# prints out to cvs
				if myDict:
					# If data is present, write to the CSV
					writer.writerow(myDict)
					myDict['state'] = x
					print(response.json())
					print(myDict)
				else:
					print(f"No data found for date {date_variable}")

				# increase day count, but keep formating okay for string
				j = j + 1
				if j < 10:
					day_variable = "0" + str(j)  # Convert the number to a string and concatenate
				else:
					day_variable = str(j)  # If number >= 10, just convert it to a string

			i = i + 1
			if i < 10:
				month_variable = "0" + str(i)  # Convert the number to a string and concatenate
			else:
				month_variable = str(i)  # If number >= 10, just convert it to a string

# PRINTING OUT RESPONSES******************
	#print(response.json())
	# print(response.json().get("data"))
	# print(response.json()['data']['date'])
	# print("confirmed",response.json()['data']['confirmed'])
	# print(response.json()['data']['deaths'])