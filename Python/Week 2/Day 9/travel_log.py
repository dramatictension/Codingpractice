#Adding a new dictionary to the list of travel_log


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


#Defines a new function that takes 3 inputs
def add_new_country(country_visited, times_visited, city_visited):
    #Make new dictionary to add
    new_country = {}
    #Add new keys called from country_visited, times_visited and city_visited
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = city_visited
    #city_visited was already added as a list, therefore does NOT require special treatment here!!

    #Append the new dictionary to the list of travel_log
    travel_log.append(new_country)

#Call the function of add_new_country with the values to append
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#print travel_log to check results
print(travel_log)
