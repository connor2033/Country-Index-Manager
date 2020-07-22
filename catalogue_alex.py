from country import Country

class CountryCatalogue:
    def __init__(self, fileOne, fileTwo):
        self.countryCat = []
        self.cDictionary = {}

        countryInfo = open(fileOne, "r")
        countryCont = open(fileTwo, "r")

        for line in countryCont:
            line = line.split(",")
            line[1] = line[1].strip("\n")
            self.cDictionary[line[0]] = line[1]

        for line in countryInfo:
            line = line.replace(",", "")
            line = line.split("|")
            line[2] = line[2].strip("\n")
            for key in self.cDictionary:
                if key == line[0]:
                    line.append(self.cDictionary[key])

            country = Country(line[0], int(line[1]), float(line[2]), line[3])
            self.countryCat.append(country)

    def findCountry(self, countryName):
        for countryObj in self.countryCat:
            if countryObj.getName() == countryName:
                return countryObj

    def setPopulationOfCountry(self, countryName, newPop):
        if self.findCountry(countryName):
            self.findCountry(countryName).setPopulation(newPop)
            return True
        else:
            return False

    def setAreaOfCountry(self, countryName, newArea):
        if self.findCountry(countryName):
            self.findCountry(countryName).setArea(newArea)
            return True
        else:
            return False

    def addCountry(self, countryName, pop, area, continent):
        if not self.findCountry(countryName):
            self.cDictionary[countryName] = continent
            newCountry = Country(countryName, pop, area, continent)
            self.countryCat.append(newCountry)
            return True
        else:
            return False

    def deleteCountry(self, countryName):
        if self.findCountry(countryName):
            self.cDictionary.pop(countryName)
            self.countryCat.remove(self.findCountry(countryName))

    def printCountryCatalogue(self):
        print(self.countryCat)

    def getCountriesByContinent(self, continentName):
        continentList = []
        for country in self.countryCat:
            if country.getContinent() == continentName:
                continentList.append(country)
        return continentList

    def getCountriesByPopulation(self, continent=""):
        countryList = []
        if continent == "":
            for country in self.countryCat:
                pair = (country.getName(), country.getPopulation())
                countryList.append(pair)
            countryList.sort(key=lambda x: x[1], reverse=True)
            return countryList
        else:
            for country in self.getCountriesByContinent(continent):
                pair = (country.getName(), country.getPopulation())
                countryList.append(pair)
            countryList.sort(key=lambda x: x[1], reverse=True)
            return countryList

    def getCountriesByArea(self, continent=""):
        countryList = []
        if continent == "":
            for country in self.countryCat:
                pair = (country.getName(), country.getArea())
                countryList.append(pair)
            countryList.sort(key=lambda x: x[1], reverse=True)
            return countryList
        else:
            for country in self.getCountriesByContinent(continent):
                pair = (country.getName(), country.getArea())
                countryList.append(pair)
            countryList.sort(key=lambda x: x[1], reverse=True)
            return countryList

    def findMostPopulousContinent(self):
        highestPop = 0
        highestContinent = ""
        continentList = []
        for continent in self.cDictionary.values():
            if continent not in continentList:
                continentList.append(continent)
        #print(continentList)
        for continent in continentList:
            population = 0
            countryList = self.getCountriesByPopulation(continent)
            #print(countryList)
            for item in countryList:
                population += item[1]
            if population > highestPop:
                highestPop = population
                highestContinent = continent
        return highestContinent, highestPop

    def filterCountriesByPopDensity(self, lowBound, upBound):
        countryList = []
        for country in self.countryCat:
            if lowBound <= country.getPopDensity() <= upBound:
                countryPair = (country.getName(), country.getPopDensity())
                countryList.append(countryPair)
        return countryList

    def saveCountryCatalogue(self, fileName):
        self.countryCat.sort(key=lambda x: x.name)
        file = open(fileName, "w")
        itemsWritten = 0
        for country in self.countryCat:
            file.write("%s|%s|%d|%.2f|%.2f\n" % (country.getName(), country.getContinent(), country.getPopulation(), country.getArea(), country.getPopDensity()))
            itemsWritten += 1
        if itemsWritten > 0:
            return itemsWritten
        else:
            return -1

test = CountryCatalogue("data.txt", "continent.txt")

print(test.filterCountriesByPopDensity(10,99999))
