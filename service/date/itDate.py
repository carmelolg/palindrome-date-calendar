#!/usr/bin/python3

from service.date.date import AbstractDate

class ITDate(AbstractDate):
    def compileDate(self, year, month, day):
        return day + '-' + month + '-' + year
    def formatDate(self):
        return '%d-%m-%Y'

