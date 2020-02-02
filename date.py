#!/usr/bin/python

from constants import Constants
import timeit

class DateUtil(object):
    years = []
    months = []
    daysOfLongMonth = []
    daysOfNormalMonth = []
    daysOfShortMonth = []
    daysOfShortMonthBissextile = []
    const = Constants()
    
    def _init(self):
        for x in range(self.const.startYear, self.const.endYear + 1):
	        self.years.append(str(x))

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

    def getAllITDate(self):
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
                    currentDate = day + '-' + month + '-' + year
                    if currentDate not in dates:
                        dates.append(currentDate)
        return dates

    def getAllI18NDate(self):
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
                    currentDate = year + '-' + month + '-' + day
                    if currentDate not in dates:
                        dates.append(currentDate)
        return dates

    def equalsBetweenITAndI18NDate(self, itDate, i18nDate):
        itYear = itDate[6:]
        itMonth = itDate[3:5]
        itDay = itDate[:2]
        
        i18nYear = i18nDate[:4]
        i18nMonth = i18nDate[5:7]
        i18nDay = i18nDate[-2:]
        
        if itYear == i18nYear and itMonth == i18nMonth and itDay == i18nDay :
            return True
        else: return False

