#!/usr/bin/python3

from service.calculate import Calculate
from service.date.itDate import ITDate
from service.date.i18nDate import I18NDate
from config.constants import Constants
from service.print import Print
import argparse

# Step 1 - Declaration phase

parser = argparse.ArgumentParser(description='Palindrome date calculation')
parser.add_argument("--start", default=2000, type=int, help="The first year")
parser.add_argument("--end", default=2030, type=int, help="The last year")

args = parser.parse_args()
fromDate = args.start
toDate = args.end

const = Constants.getInstance()
justPrint = Print()
calculate = Calculate()
itDate = ITDate()
i18nDate = I18NDate()

# Step 2 - Data preparation

const.startYear = fromDate
const.endYear = toDate
itDates = itDate.getAllDate()
i18nDates = i18nDate.getAllDate()

# Step 3 - Calculation

itCalculation = calculate.getPalindromeDate(itDates)
i18nCalculation = calculate.getPalindromeDate(i18nDates)
commonCalculation = calculate.getPalindromeDateInCommon(itCalculation['dates'], i18nCalculation['dates'])

itNextDateResult = calculate.getNextPalindromeDate(itCalculation['dates'], itDate.formatDate())
itLastDateResult = calculate.getLastPalindromeDate(itCalculation['dates'], itDate.formatDate())
i18nNextDateResult = calculate.getNextPalindromeDate(i18nCalculation['dates'], i18nDate.formatDate())
i18nLastDateResult = calculate.getLastPalindromeDate(i18nCalculation['dates'], i18nDate.formatDate())

# Step 4 - Console output

justPrint.title()
justPrint.header()
justPrint.stats('Italian standard in statistics', itNextDateResult['distance'], itNextDateResult['date'], itLastDateResult['distance'], itLastDateResult['date'])
justPrint.stats('International standard in statistics', i18nNextDateResult['distance'], i18nNextDateResult['date'], i18nLastDateResult['distance'], i18nLastDateResult['date'])
justPrint.dates('International and italian intersection', commonCalculation['count'], commonCalculation['dates'])
justPrint.dates('Italian standard', itCalculation['count'], itCalculation['dates'])
justPrint.dates('International standard', i18nCalculation['count'], i18nCalculation['dates'])
justPrint.footer()

