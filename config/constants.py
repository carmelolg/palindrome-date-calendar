#!/usr/bin/python3

class Constants(object):
    longMonths = ['01', '03', '05', '07', '08', '10', '12']
    normalMonths = ['11','04','06', '09']
    shortMonths = ['02']
    startYear = 0
    endYear = 10000
    numMonths = 12
    numDaysShortMonth = 28
    numDaysNormalMonth = 30
    numDaysLongMonth = 31
    numDaysShortMonthBissextile = 29

    __instance = None
    @staticmethod
    def getInstance():
        if Constants.__instance == None:
            Constants()
        return Constants.__instance
    def __init__(self):
        if Constants.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Constants.__instance = self

