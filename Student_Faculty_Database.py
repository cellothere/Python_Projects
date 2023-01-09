#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 09:42:01 2022

@author: paulbergeron
"""

import datetime

class Person(object):
    def __init__(self, name):
        
        self.name = name
        self.birthday = None
        self.lastname = name.split(' ')[-1]
    def getLastName(self):
        return self.lastname
    def __str__(self):
        return self.name
    def setBirthday(self,month, day, year):
        self.birthday = datetime.date(year, month, day)
    def setAge(self):
        if self.birthday == None:
            raise ValueError
        return(datetime.date.today()-self.birthday).days
    def __lt__(self, other):
        if self.lastname == other.lastname:
            return self.name < other.name
        return self.lastname < other.lastname
    
    
class YSUPerson(Person):
    nextIDNum = 0
   
    def __init__(self,name):
        Person.__init__(self, name)
        self.IDNum = YSUPerson.nextIDNum
        YSUPerson.nextIDNum +=1
    def getIDNum(self):
        return self.IDNum
    def __lt__(self, other):
        return self.IDNum < other.IDNum
    def speak(self, utterance):
        return (self.getLastName() + ' says: ' + utterance)

class Student(YSUPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        YSUPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    def speak(self, utterance):
        return YSUPerson.speak(self, "dude, " + utterance)
    
class Grad(Student):
    pass

class transferStudent(Student):
    pass 

class Professor(YSUPerson):
    def __init__(self, name, department):
        YSUPerson.__init__(self, name)
        self.department = department
    def speak(self, utterance):
        new = ('in course ' + self.department + " we say ")
        return YSUPerson.speak(self, new + utterance)
    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)

def isStudent(obj):
    return isinstance(obj, Student) 



s1 = UG("Paul Bergeron", 2017)
s2 = UG('Jessica Schmidt', 2018)
s3 = Grad("Foo Bar")
faculty = Professor("Dr Livingstone", 'six')


