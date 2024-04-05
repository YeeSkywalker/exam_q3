'''
    The code can be accessed on GitHub: https://github.com/YeeSkywalker/exam_q3
    Set up:
    1. Ensure you have Python version later than 3.4.

    2. Install virtual environment by running the following command in the terminal:
        python3 -m venv env

    3. Access the virtual environment:
        source env/bin/activate

    4. Install the requests library to fetch data from the RESTful API:
        pip3 install requests

    5. Compile the code:
        python3 q3.py
'''

import requests
import statistics
url = "https://restcountries.com/v3.1/all" # Restful API url

# Q3
def Q3():
    densities = [] # Global varaiable for density caculation

    # Part1: For each country, the country name and its population density (population per unit area).
    def part1():
        nonlocal densities
        partOneUrl = url + "?fields=name,population,area" # Filter reponse based on feilds name, population, area
        try:
            response = requests.get(partOneUrl) # Send the GET request to API
            if response.status_code == 200: # If get the response successfully
                data = response.json() 
                h = ['Country', 'Density']
                print('{:<50s} {:<50s}'.format(*h))
                for countryData in data:
                    name = countryData.get('name', 'N/A').get('common', 'N/A') # Get the common name of current country; if not exist, return N/A
                    population = countryData.get('population', 0) # Get the population of current country; if not exist, return 0
                    area = countryData.get('area', 1) # Get the area of current country; if not exist, return 0
                    density = population / area # Caculate the density of current country
                    densities.append(density) # Save density for Part2
                    print('{:<50s} {:<10f}'.format(*[name, density]))
            else:
                print(f"Error: Status code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

    # Part2: The mean, median and standard deviation of the population density.
    def part2():
        nonlocal densities
        # If successfully get response from API in Part 1
        if densities:
            print(f"The mean of population density is: {statistics.mean(densities)}") # Print mean of density
            print(f"Then median of population density is: {statistics.median(densities)}") # Print median of density
            print(f"The standard deviation of population density is: {statistics.pstdev(densities)}") # Print standard deviation of density
        else:
            print(f"Failed to fetch data from API")
    
    # Part3: The number of countries who are UN members, and the number of countries who use the Euro as a currency.
    def part3():
        unMembers = 0 # Count number of UN members
        euroCurrency = 0 # Count number of countries using Euro
        partThreeUrl = url + "?fields=unMember,currencies" # Filter reponse based on feilds unMember, currencies
        try:
            response = requests.get(partThreeUrl) # Send the GET request to API
            if response.status_code == 200: # If get the response successfully
                data = response.json()
                for countryData in data:
                    isMember = countryData.get('unMember', False) # Check if current country / area is UN members
                    currency = countryData.get('currencies', {}).get('EUR', None) # Check if current country / area using Euro
                    unMembers += 1 if isMember else 0 # If current country is UN member, add 1 to the count
                    euroCurrency += 1 if currency else 0 # If current region is using euro, add 1 to the count
                print(f"The number of countries who are UN members is: {unMembers}")
                print(f"The number of (independent or not independent) countries who use the Euro as a currency: {euroCurrency}")
            else:
                print(f"Error: Status code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

    print(f"==========Q3 Part1==========")
    part1()
    print(f"==========Q3 Part2==========")
    part2()
    print(f"==========Q3 Part3==========")
    part3()
    print(f"==========End of Q3==========")

Q3()