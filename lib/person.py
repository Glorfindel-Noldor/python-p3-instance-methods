#!/usr/bin/env python3

class Person:
    def __init__(self):
        self.talking = "Hello World!"
        self.walking = "The person is walking."

    def talk(self):
        print(self.talking)
    def walk(self):
        print(self.walking)