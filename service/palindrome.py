#!/usr/bin/python3

class Palindrome(object):
	def isPalindrome(self, date):
		_date = date.replace('-', '')
		inverse = _date[::-1]
		return True if inverse == _date else False
