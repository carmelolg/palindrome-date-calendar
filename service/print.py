#!/usr/bin/python3

from config.constants import Constants

class Print(object):
    const = Constants.getInstance()

    def pad(self, string):
        return "{:<50}".format(string)

    def field(self, field):
        print("- ", self.pad(field), " -")

    def divisor(self):
        print('--------------------------------------------------------')

    def space(self):
        self.field(' ')

    def title(self):
        self.divisor()
        print('-                    PALINDROME DATE                   -')
        self.divisor()

    def header(self):
        print('-                 FROM ',str(self.const.startYear).zfill(4) ,' TO ',str(self.const.endYear).zfill(4),'                -')
        self.divisor()

    def footer(self):
        self.space()
        self.field('Thanks for taking your time, @carmelolg')
        self.space()
        self.divisor()

    def dates(self, title, count, fields):
        self.space()
        self.field(title)
        self.space()
        self.field('Number of palindrome dates: ' + str(count))
        self.field('List')
        for field in fields:
            self.field(field)
        self.space()
        self.divisor()

    def stats(self, title, nextCount, nextField, lastCount, lastField):
        self.space()
        self.field(title)
        self.space()
        self.field('Next: ' + nextField + ' in ' + str(nextCount) + ' days')
        self.field('Last: ' + lastField + ' ' + str(lastCount) + ' days ago')
        self.space()
        self.divisor()