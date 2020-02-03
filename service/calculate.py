#!/usr/bin/python3

from service.palindrome import Palindrome
from service.date.dateUtils import DateUtil

class Calculate(object):
    palindromeUtils = Palindrome()
    utils = DateUtil()
    def getPalindromeDate(self, dates):
        count = 0
        palindromeDate = []
        result = dict()
        for date in dates:
            if self.palindromeUtils.isPalindrome(date):
                count += 1
                palindromeDate.append(date)
        
        result['count'] = count
        result['dates'] = palindromeDate
        return result

    def getPalindromeDateInCommon(self, itPalindromeDate, i18nPalindromeDate):
        count = 0;
        palindromeDate = []
        result = dict()
        
        for itDate in itPalindromeDate:
            for i18nDate in i18nPalindromeDate:
                if self.utils.equalsBetweenITAndI18NDate(itDate, i18nDate):
                    count += 1
                    palindromeDate.append(itDate + '|' + i18nDate)

        result['count'] = count
        result['dates'] = palindromeDate
        return result
    
