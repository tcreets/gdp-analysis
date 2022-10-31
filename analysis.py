import csv

# save each row into a list (TODO: change to your path!)
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"


# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"

def get_state_gdp(data, state, year):
    for d in data:
        if d["GeoName"] == state:
            return float(d[year])

def get_highest_gdp(data, year):
    highest = float("-inf")
    highestGDPState = ""
    for d in data:
        value = float(d[year])
        if value > highest:
            highest = value
            highestGDPState = d['GeoName']
    return highestGDPState

def get_lowest_gdp(data, year):
    lowest = float("inf")
    lowestGDPState = ""
    for d in data:
        value = float(d[year])
        if value < lowest:
            lowest = value
            lowestGDPState = d['GeoName']
    return lowestGDPState

#Challenge 2
def get_percent_change(data, state, year1, year2):
    y1GDP = get_state_gdp(data, state, year1)
    y2GDP = get_state_gdp(data, state, year2)
    percentChange = (y2GDP - y1GDP)/y1GDP
    return percentChange

#Challenge 1
highestGDP_years = {"Year": "State with the highest GDP"}
lowestGDP_years = {"Year": "State with the lowest GDP"}
for i in range(1997,2021):
    i = str(i)
    hgdpForYear = get_highest_gdp(list_data,i)
    lgdpForYear = get_lowest_gdp(list_data, i)
    highestGDP_years[i] = hgdpForYear
    lowestGDP_years[i] = lgdpForYear
    


with open("highest_gdp_per_year.csv", "w") as infile:
    writer = csv.DictWriter(infile, fieldnames = list(highestGDP_years.keys()))
    writer.writeheader()
    writer.writerows([highestGDP_years, lowestGDP_years])


#print(get_highest_gdp(list_data, '2020'))
#print(get_lowest_gdp(list_data, '2020'))
print(get_percent_change(list_data, "New York",'2019', '2020'))
#print(highestGDP_years)
#print(lowestGDP_years)