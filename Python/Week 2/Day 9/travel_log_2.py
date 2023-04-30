#Adding a new dictionary to the list of travel_log, asking the user for input


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

def add_new_country():
    country_visited = input("What Country have you visited? \n")
    print("\n")
    times_visited = input("How many times have you visited? \n")
    print("\n")
    city_visited_list = input("What cities have you visited? Seperate with space. \n")
    print("\n")
    while "," in city_visited_list:
        print("Don't add commas!")
        city_visited_list = input("What cities have you visited? Seperate with space. \n")
    city_visited = city_visited_list.split()

    #Make new dictionary to add
    new_country = {}
    #Add new keys called from country_visited, times_visited and city_visited
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = city_visited
    #city_visited was already added as a list, therefore does NOT require special treatment here!!

    #Append the new dictionary to the list of travel_log
    travel_log.append(new_country)

#Call the function of add_new_country
add_new_country()
#print travel_log to check results
print(travel_log)
