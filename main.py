#!/usr/bin/python3

from service.calculate import Calculate
from service.date.itDate import ITDate
from service.date.i18nDate import I18NDate
from config.constants import Constants
#import timeit

calculate = Calculate()
itDate = ITDate()
i18nDate = I18NDate()
const = Constants()

#timePrepareStart = timeit.default_timer()

itDates = itDate.getAllDate()
i18nDates = i18nDate.getAllDate()

#timePrepareStop = timeit.default_timer()

#print 'Preparation elapsed time: ', timePrepareStop - timePrepareStart

itCalculation = calculate.getPalindromeDate(itDates)
i18nCalculation = calculate.getPalindromeDate(i18nDates)
commonCalculation = calculate.getPalindromeDateInCommon(itCalculation['dates'], i18nCalculation['dates'])

# Console output

print('--------------------------------------------------------')
print('-                    PALINDROME DATE                   -')
print('-                   FROM ',str(const.startYear),' TO ',str(const.endYear),'                  -')
print ('-                                                      -' )
print ('- Italian standard                                     -' )
print ('-                                                      -')
print ('- Number of palindrome dates: ', str(itCalculation['count']), '                        -')
print ('- List                                                 -')
for x in itCalculation['dates']:
    print ('- '+ str(x), '                                           -')
print ('-                                                      -')
print ('--------------------------------------------------------')


print ('- International standard                               -' )
print ('-                                                      -')
print ('- Number of palindrome dates: ', str(i18nCalculation['count']), '                        -')
print ('- List                                                 -')
for x in i18nCalculation['dates']:
    print ('- '+ str(x), '                                           -')
print ('-                                                      -')
print ('--------------------------------------------------------')

print ('- International and italian intersection               -' )
print ('-                                                      -')
print ('- Number of palindrome dates: ', str(commonCalculation['count']), '                        -')
print ('- List                                                 -')
for x in commonCalculation['dates']:
    print ('- '+ str(x), '                                -')
print ('-                                                      -')
print ('--------------------------------------------------------')
