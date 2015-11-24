# -*- coding: utf-8 -*-


import csv
import string

class Coffee(object):
    """A class to hold information about coffees"""
    def __init__(self, roaster, name, chars, desc):
        self.roaster = roaster
        self.name = name
        self.chars = chars
        self.desc = desc

    def getRoaster(self):
        return self.roaster

    def getName(self):
        return self.name

class Score(object):
    """A class to hold each coffee's score"""
    def __init__(self, roaster, name, score):
        self.roaster = roaster
        self.name = name
        self.score = score

    def getRoaster(self):
        return self.roaster

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

def cmpScores(a,b):
    if (a.getScore() - b.getScore()) < 0:
        return 1
    if (a.getScore() - b.getScore()) > 0:
        return -1
    else:
        return 0

def printCoffees(data):
    count = 1
    print("Available coffees:")
    for row in data:
        print str(count) + ") " + row[0] + " -- " + row[1]
        count += 1

with open('first_sheet_BB.tsv', 'rb') as dataFile:
    data = csv.reader(dataFile, delimiter='\t')
    list = []
    for row in data:
        list.append(Coffee(row[0], row[1], row[2], row[3]))


    printCoffees(data)
    print "Make a selection: "
    coffee = raw_input()
    dataFile.seek(0)

    name = "Hayes Valley Espresso"
    origin = ""
    chars = "Cocoa, orange zest, smoky finish"
    desc = "We developed this espresso over five years ago for the launch of our Kiosk on Linden Street. This is probably our darkest espresso: lower-toned, minimal brightness, plenty of chocolate – with an engaging complexity as a straight shot. The shots are gorgeous: achingly heavy with voluptuous red-brown crema, and the silky, somewhat dangerous-looking viscosity of a power-steering stop-leak product once used on our (now departed) heroically battered 1983 Peugeot. In milk, it tastes like chocolate ovaltine, and holds its own from the daintiest 3oz Macchiato to our towering 12oz caffe latte. This is the most Brahmsian espresso we have. Brooding and autumnal, it is a coffee to mourn the passing of time."

    nSet = set(name.lower().split(" "))
    oSet = set(origin.lower().split(" "))
    cSet = set(chars.lower().split(" "))
    dSet = set(desc.lower().split(" "))

    scores = []

    for row in data:
        nSet2 = set(row[1].lower().split(" "))
        oSet2 = set(row[2].lower().split(" "))
        cSet2 = set(row[3].lower().split(" "))
        dSet2 = set(row[4].lower().split(" "))

        nameScore    = (len(nSet.intersection(nSet2)) / float(len(nSet.union(nSet2)))) * .00
        originScore  = (len(oSet.intersection(oSet2)) / float(len(oSet.union(oSet2)))) * .00
        charsScore   = (len(cSet.intersection(cSet2)) / float(len(cSet.union(cSet2)))) * .45
        descScore    = (len(dSet.intersection(dSet2)) / float(len(dSet.union(dSet2)))) * .55
        total = nameScore + originScore + charsScore + descScore


        scores.append(Score(row[0], row[1], total))
        #print str(nameScore)+" "+str(originScore)+" "+str(charsScore)+" "+str(descScore)
        #print(row[1] + "\t" + str(nameScore + originScore + charsScore + descScore))

scores.sort(cmp=cmpScores)

count = 0
index = 0

print "You may like:"
while (count < 3):
    if scores[index].getName() != name:
        print scores[index].getRoaster() + " -- " + scores[index].getName() + " -- " + str(scores[index].getScore())
        count += 1
    index += 1
