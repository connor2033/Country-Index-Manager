from country import Country

class CountryCatalogue:

    # This initialising method creates string variables which contain the file names inputted by the user.
    # It also creates the list called "countryCat" and the dictionary called "cDictionary".
    def __init__(self, firstFile, secondFile):
        self.countryCat = []
        self.cDictionary = {}

    # This is where I open the files based on the file names given and turn them each into a list.
        countryInfo = open(firstFile, "r")
        CountryContinent = open(secondFile, "r")
        countryInfo = countryInfo.readlines()
        CountryContinent = CountryContinent.readlines()

        # Here I'm formatting the list of continents and countries (Country,Continent), to remove the comas and the "\n".
        # I then add each line of the file into the dictionary "cDictionary".
        # I use the "[1:]" in my for loop to skip the first line of the file (the header).
        for line in CountryContinent[1:]:
            line = line.split(",")
            line[1] = line[1].strip("\n")
            self.cDictionary[line[0]] = line[1]

        # Here I format the list of countries (Country|Population|Area)  by removing any commas from numbers (so python will recognize them) and splitting them into lists separated by "|".
        # I then append it into the cDictionary (Country,Continent)
        # I use the "[1:]" in my for loop to skip the first line of the file (the header).
        for line in countryInfo[1:]:
            line = line.replace(",", "")
            line = line.split("|")
            line[2] = line[2].strip("\n")
            for i in self.cDictionary:
                if i == line[0]:
                    line.append(self.cDictionary[i])

            countryItem = Country(line[0], int(line[1]), float(line[2]), line[3])
            self.countryCat.append(countryItem)

    # For this method, I simply loop through the entire countryCat, and if the inputted name equals the name in the catalogue, it returns the country object.
    def findCountry(self, name):
        for country in self.countryCat:
            if country.getName() == name:
                return country

    # Here, I use the previous "findCountry" method to find the inputted country, then use the ".setPopulation()" method from the country class if the country exists.
    def setPopulationOfCountry(self, name, newPop):
        if self.findCountry(name):
            self.findCountry(name).setPopulation(newPop)
            return True
        else:
            return False

    # This method is almost identical to the previous method, except it uses the ".setArea()" method from the country class instead.
    def setAreaOfCountry(self, name, newArea):
        if self.findCountry(name):
            self.findCountry(name).setArea(newArea)
            return True
        else:
            return False

    # This method has name, population, area/size and continent all as parameters. It first checks to make sure that the country doesn't already exist,
    # and then creates a new variable called "newCountry" which it makes into a country object that uses all of the above parameters and appends the country to the catalogue.
    # Finally, it appends the country name and continent to the "cDictionary" and returns "True" if the country was successfully added.
    def addCountry(self, name, pop, area, continent):
        if not self.findCountry(name):
            newCountry = Country(name, pop, area, continent)
            self.countryCat.append(newCountry)
            self.cDictionary[name] = continent
            return True
        else:
            return False

    # First I check to make sure that the country exists by using the "findCountry" method, I then remove it from the cDictionary and the countryCat.
    def deleteCountry(self, name):
        if self.findCountry(name):
            self.cDictionary.pop(name)
            self.countryCat.remove(self.findCountry(name))

    # Here I simply print the country catalogue when this method is called.
    def printCountryCatalogue(self):
        print(self.countryCat)

    # Here I first create a list called "contList" where I will store the names of all of the countries in a specified continent.
    # I then loop through the countryCat and if the inputted continent name equals the country.getContinent(), I append the country to the continent list.
    def getCountriesByContinent(self, continentName):
        contList = []
        for country in self.countryCat:
            if country.getContinent() == continentName:
                contList.append(country)
        return contList

    # Here I take an input of the name of a continent (or nothing), and if the continent exists, I create a list of tuples that have the country name and population in them.
    # I then return that list once I put it in descending order by population.
    # If no continent is specified, I return a list tuples of all of the countries in descending order.
    def getCountriesByPopulation(self, contName=""):
        countries = []
        if contName == "":
            for i in self.countryCat:
                Ctup = (i.getName(), i.getPopulation())
                countries.append(Ctup)
            countries = sorted(countries, key=lambda x: x[1], reverse=True)
            return countries
        else:
            for i in self.getCountriesByContinent(contName):
                Ctup = (i.getName(), i.getPopulation())
                countries.append(Ctup)
                countries = sorted(countries, key=lambda x: x[1], reverse=True)
            return countries

    # This method is almost identical to the previous one, however it uses the .getArea() method instead.
    def getCountriesByArea(self, contName=""):
        countries = []
        if contName == "":
            for i in self.countryCat:
                Ctup = (i.getName(), i.getArea())
                countries.append(Ctup)
            countries = sorted(countries, key=lambda x: x[1], reverse=True)
            return countries
        else:
            for i in self.getCountriesByContinent(contName):
                Ctup = (i.getName(), i.getArea())
                countries.append(Ctup)
                countries = sorted(countries, key=lambda x: x[1], reverse=True)
            return countries

    # In this method, I first loop through the cDictionary to compile a list of all the continents that currently exist.
    # I then run each continent in that list through the "getCountriesByPopulation" method and add all of the individual country's populations
    # together to get a total continent population. I have a variable named "biggest pop" which I use to keep track of which continent has the largest
    # population, simply by comparing them in an if statement. I finally output a tuple containing the name of the biggest continent and the population of that continent.
    def findMostPopulousContinent(self):
        continents = []
        biggestPop = 0
        biggestContinent = ""

        for continent in self.cDictionary.values():
            if continent not in continents:
                continents.append(continent)
        for continent in continents:
            pop = 0
            countries = self.getCountriesByPopulation(continent)
            for country in countries:
                pop += country[1]
            if pop > biggestPop:
                biggestPop = pop
                biggestContinent = continent
        finalTuple = (biggestContinent, biggestPop)
        return finalTuple

    # Here I have the minimum population and maximum population as parameters for the method. I simply loop through the countryCat and append country objects within
    # the specified range to a list called "countryList". Finally, I use the "sorted" function to put the countries in the proper order and output the countryList.
    def filterCountriesByPopDensity(self, min, max):
        countryList = []
        for country in self.countryCat:
            if min <= country.getPopDensity() <= max:
                countryTup = (country.getName(), country.getPopDensity())
                countryList.append(countryTup)
                countryList = sorted(countryList, key=lambda x: x[1], reverse=True)
        return countryList

    # This method first sorts the countryCat, and then creates a file who's name is specified by input (parameter) and writes the entire catalogue, line by line, into that file.
    # It also keeps track of how many items were added to the file and returns the number once the file is writen.
    def saveCountryCatalogue(self, fileName):
        self.countryCat.sort(key=lambda x: x.name)
        file = open(fileName, "w")
        itemsAdded = 0
        for country in self.countryCat:
            file.write("{}|{}|{}|{}|{}".format(country.getName(), country.getContinent(), country.getPopulation(), country.getArea(), country.getPopDensity()))
            file.write("\n")
            itemsAdded += 1
        if itemsAdded > 0:
            return itemsAdded
        else:
            return -1




