#!/usr/bin/python3

from config.constants import Constants
from service.date.dateUtils import DateUtil
from abc import ABC, abstractmethod

class AbstractDate(ABC):
    years = []
    months = []
    daysOfLongMonth = []
    daysOfNormalMonth = []
    daysOfShortMonth = []
    daysOfShortMonthBissextile = []
    const = Constants.getInstance()
    utils = DateUtil()

    @abstractmethod
    def compileDate(self, year, month, day):
        pass

    @abstractmethod
    def formatDate(self):
        pass
    
    def _init(self):
        for x in range(self.const.startYear, self.const.endYear + 1):
            _x = str(x).zfill(4)
            if self.utils.isYearValid(_x):
	            self.years.append(_x)

        for x in range(1, self.const.numMonths + 1):
            self.months.append(self._initNumber(x))

        for x in range(1, self.const.numDaysLongMonth + 1):
	        self.daysOfLongMonth.append(self._initNumber(x))

        for x in range(1, self.const.numDaysNormalMonth + 1):
	        self.daysOfNormalMonth.append(self._initNumber(x))

        for x in range(1, self.const.numDaysShortMonth + 1):
	        self.daysOfShortMonth.append(self._initNumber(x))

        for x in range(1, self.const.numDaysShortMonthBissextile + 1):
	        self.daysOfShortMonthBissextile.append(self._initNumber(x))        
    
    def _initNumber(self, number):
        return '0' + str(number) if number < 10 else str(number)

    def getAllDate(self):
        self._init()
        dates = []
        for year in self.years:
            bissexTileYear = True if int(year) % 4 == 0 else False
            _daysOfShortMonth = self.daysOfShortMonthBissextile if bissexTileYear else self.daysOfShortMonth
            for month in self.months:
                days = self.daysOfLongMonth
                if month in self.const.shortMonths:
                    days = _daysOfShortMonth
                elif month in self.const.normalMonths:
                    days = self.daysOfNormalMonth
                for day in days:
                    currentDate = self.compileDate(year, month, day)
                    if currentDate not in dates:
                        dates.append(currentDate)
        return dates

