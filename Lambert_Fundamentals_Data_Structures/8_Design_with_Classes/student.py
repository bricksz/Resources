'''
File: student.py
Resources to manage a student's name and test scores.
'''

import functools

class Student(object):
    def __init__(self, name, number):
        ''' Constructor creates a Student with the given name and number
        of scores and sets all scores to 0. '''
        self._name = name
        self._scores = []
        for count in range(number):
            self._scores.append(0)

    def getName(self):
        ''' Returns the student's name. '''
        return self._name

    def setScore(self, i, score):
        ''' Resets the i-th score, counting from 1. '''
        self._scores[i - 1] = score

    def getScore(self, i):
        ''' Returns the i-th score, counting from 1. '''
        return self._scores[i - 1]

    def getAverage(self):
        ''' Returns the average score. '''
        sum = functools.reduce(lambda x, y: x + y, self._scores)
        return sum / len(self._scores)

    def getHighScore(self):
        ''' Returns the highest score. '''
        return max(self._scores)

    def __str__(self):
        ''' Returns the string representation of the student. '''
        return "Name: " + self._name + "\nScores: " + \
            " ".join(map(str, self._scores))


