#!/usr/bin/python3

from service.date.date import AbstractDate

class I18NDate(AbstractDate):
    def compileDate(self, year, month, day):
        return year + '-' + month + '-' + day
