# My name is Connor Haines and this is a multi file program designed to take file names as inputs to form a catalogue
# of countries. This program also allows for editing of each type of information stored about a country (Population, Area, Continent, etc.)
# The user also has the ability to add or remove countries, as well as look up key information.


class Country:
    # This initialization method defines a "Country" as an object that contains a name, population, area and continent.
    def __init__(self, name, population, area, continent):
        self.name = name
        self.population = population
        self.area = area
        self.continent = continent


# The following 4 "getter methods" are used to retrieve information about Country objects (such as name, population, area and continent.)
    def getName(self):
        return self.name

    def getPopulation(self):
        return self.population

    def getArea(self):
        return self.area

    def getContinent(self):
        return self.continent


# The following 3 methods are used to change the information of any "Country" object. You can change population, area and continent.

    def setPopulation(self, newPopulation):
        self.population = newPopulation

    def setArea(self, newArea):
        self.area = newArea

    def setContinent(self, newContinent):
        self.continent = newContinent

# This getter method is last, because it is used to get the population density, which actually requires access to the population and the size.
    def getPopDensity(self):
        return round(self.population / self.area, 2)

# This represent method is what is used for the output of any Country object.
    def __repr__(self):
        return "{} (pop: {}, size: {}) in {}".format(self.name, self.population, self.area, self.continent)





