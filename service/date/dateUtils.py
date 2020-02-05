#!/usr/bin/python3

import datetime

class DateUtil(object):
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

    def isYearValid(self, year):
        return True if int(year[:2][::-1]) <= 12 and int(year[:2][::-1]) > 0 and int(year[2:][::-1]) > 0 and int(year[2:][::-1]) <= 31 else False

    def daysBetweenTwoDatesInString(self, d1, d2, format):
        d1 = datetime.strptime(d1, format)
        d2 = datetime.strptime(d2, format)
        return abs((d2 - d1).days)
    
    def daysBetweebTwoDates(self, d1, d2):
        return abs((d2 - d1).days)