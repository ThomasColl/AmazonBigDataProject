import yearlyDatatype
import matplotlib.pyplot as plt

class normalisedDatatype:
    def __init__(self):
        self.dictOfYears = {}

    def addYear(self, yearlyData):
        self.dictOfYears[yearlyData.year] = yearlyData

    def isYearThere(self, year):
        if year in self.dictOfYears:
            return True
        else:
            return False

    def orderYears(self):
        return sorted(self.dictOfYears)

    def getAnnualAverages(self):
        for key, value in self.dictOfYears.items():
            value.setAverage()

    def getPlottableDict(self):

        plottableDict = {}
        for key, value in self.dictOfYears.items():
            plottableDict[key] = value.count
        return plottableDict

    def plotCount(self):
        plottableDict = {}
        for key, value in self.dictOfYears.items():
            plottableDict[key] = value.count
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()

    def plotTotal(self):
        plottableDict = {}
        for key, value in self.dictOfYears.items():
            plottableDict[key] = value.totalScore
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()

    def plotAverage(self):
        self.getAnnualAverages()
        plottableDict = {}
        for key, value in self.dictOfYears.items():
            plottableDict[key] = value.average
        plt.scatter(range(len(plottableDict)), sorted(plottableDict.values()))
        plt.show()
