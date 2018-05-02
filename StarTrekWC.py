#!/usr/bin/python
import csv
import operator
import os
import re
import glob

picard = {}
troi = {}
riker = {}
worf = {}
data = {}
geordi = {}
wesley = {}
beverly = {}
characterDicts = [picard, troi, riker, worf, data, geordi, wesley, beverly]
names = ["PICARD", "TROI", "RIKER", "WORF", "DATA", "GEORDI", "WESLEY", "BEVERLY"]
commonWords = {"the", "be", "to", "of", "and", "in", "that", "have", "i", "it", "for", "not", "on", "with", "he", "as",
               "you", "do", "at", "", "a", "is", "by", "from"}

for filePath in glob.glob("/Users/emersonsjsu/Downloads/ScriptsTNG/*.txt"):
    file = open(filePath, "r", encoding="utf-8", errors="ignore")
    lines = file.readlines()
    for index, line in enumerate(lines):
        for name in names:
            if line.strip() == name:
                dialogueIndex = index + 1
                dialogue = lines[dialogueIndex]
                while dialogue != "\n":
                    # Skip all line with parenthesis
                    if "(" in dialogue:
                        while ")" not in dialogue:
                            dialogueIndex += 1
                            dialogue = lines[dialogueIndex]
                    else:
                        if name == "PICARD":
                            for word in dialogue.lower().split():
                                word = re.sub(r'\W+', '', word)
                                if word not in picard:
                                    picard[word] = 1
                                else:
                                    picard[word] += 1
                        elif name == "TROI":
                            for word in dialogue.lower().split():
                                word = re.sub(r'\W+', '', word)
                                if word not in troi:
                                    troi[word] = 1
                                else:
                                    troi[word] += 1
                        elif name == "RIKER":
                            for word in dialogue.lower().split():
                                word = re.sub(r'\W+', '', word)
                                if word not in riker:
                                    riker[word] = 1
                                else:
                                    riker[word] += 1
                        elif name == "WORF":
                            for word in dialogue.lower().split():
                                word = re.sub(r'\W+', '', word)
                                if word not in worf:
                                    worf[word] = 1
                                else:
                                    worf[word] += 1
                        elif name == "DATA":
                            for word in dialogue.lower().split():
                                word = re.sub(r'\W+', '', word)
                                if word not in data:
                                    data[word] = 1
                                else:
                                    data[word] += 1
                        elif name == "GEORDI":
                            for word in dialogue.lower().split():
                                word = re.sub(r'\W+', '', word)
                                if word not in geordi:
                                    geordi[word] = 1
                                else:
                                    geordi[word] += 1
                        elif name == "WESLEY":
                            for word in dialogue.lower().split():
                                word = re.sub(r'\W+', '', word)
                                if word not in wesley:
                                    wesley[word] = 1
                                else:
                                    wesley[word] += 1
                        elif name == "BEVERLY":
                            for word in dialogue.lower().split():
                                word = re.sub(r'\W+', '', word)
                                if word not in beverly:
                                    beverly[word] = 1
                                else:
                                    beverly[word] += 1
                    dialogueIndex += 1
                    dialogue = lines[dialogueIndex]
    file.close()

for characterDict in characterDicts:
    for commonWord in commonWords:
        del characterDict[commonWord]

picardSorted = sorted(picard.items(), key=operator.itemgetter(1), reverse=True)
troiSorted = sorted(troi.items(), key=operator.itemgetter(1), reverse=True)
rikerSorted = sorted(riker.items(), key=operator.itemgetter(1), reverse=True)
worfSorted = sorted(worf.items(), key=operator.itemgetter(1), reverse=True)
dataSorted = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
geordiSorted = sorted(geordi.items(), key=operator.itemgetter(1), reverse=True)
wesleySorted = sorted(wesley.items(), key=operator.itemgetter(1), reverse=True)
beverlySorted = sorted(beverly.items(), key=operator.itemgetter(1), reverse=True)

sortedLists = [picardSorted, troiSorted, rikerSorted, worfSorted, dataSorted, geordiSorted, wesleySorted, beverlySorted]

'''
for k, v in picardSorted:
    print("(" + str(k) + "," + str(v) + ")")
for k, v in troiSorted:
    print("(" + str(k) + "," + str(v) + ")")
for k, v in rikerSorted:
    print("(" + str(k) + "," + str(v) + ")")
for k, v in worfSorted:
    print("(" + str(k) + "," + str(v) + ")")
for k, v in dataSorted:
    print("(" + str(k) + "," + str(v) + ")")
for k, v in geordiSorted:
    print("(" + str(k) + "," + str(v) + ")")
for k, v in wesleySorted:
    print("(" + str(k) + "," + str(v) + ")")
for k, v in beverlySorted:
    print("(" + str(k) + "," + str(v) + ")")
'''
os.chdir("wcOutput/")

w = csv.writer(open("picard.csv", "w"))
w.writerows(picardSorted)
for k, v in picard.items():
    w.writerow([k, v])
w = csv.writer(open("troi.csv", "w"))
w.writerows(troiSorted)
for k, v in troi.items():
    w.writerow([k, v])
w = csv.writer(open("riker.csv", "w"))
w.writerows(rikerSorted)
for k, v in riker.items():
    w.writerow([k, v])
w = csv.writer(open("worf.csv", "w"))
w.writerows(worfSorted)
for k, v in worf.items():
    w.writerow([k, v])
w = csv.writer(open("data.csv", "w"))
w.writerows(dataSorted)
for k, v in data.items():
    w.writerow([k, v])
w = csv.writer(open("geordi.csv", "w"))
w.writerows(geordiSorted)
for k, v in geordi.items():
    w.writerow([k, v])
w = csv.writer(open("wesley.csv", "w"))
w.writerows(wesleySorted)
for k, v in wesley.items():
    w.writerow([k, v])
w = csv.writer(open("beverly.csv", "w"))
w.writerows(beverlySorted)
for k, v in beverly.items():
    w.writerow([k, v])
