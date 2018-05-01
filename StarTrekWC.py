#!/usr/bin/python
import operator
import re

file = open("/Users/emersonsjsu/Downloads/ScriptsTNG/102.txt", "r")
picard = {}
troi = {}
riker = {}
worf = {}
data = {}
geordi = {}
wesley = {}
beverly = {}
names = {"PICARD", "TROI", "RIKER", "WORF", "DATA", "GEORDIE", "WESLEY", "BEVERLY"}

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

picardSorted = sorted(picard.items(), key=operator.itemgetter(1), reverse=True)
troiSorted = sorted(troi.items(), key=operator.itemgetter(1), reverse=True)
rikerSorted = sorted(riker.items(), key=operator.itemgetter(1), reverse=True)
worfSorted = sorted(worf.items(), key=operator.itemgetter(1), reverse=True)
dataSorted = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
geordiSorted = sorted(geordi.items(), key=operator.itemgetter(1), reverse=True)
wesleySorted = sorted(wesley.items(), key=operator.itemgetter(1), reverse=True)
beverlySorted = sorted(beverly.items(), key=operator.itemgetter(1), reverse=True)

for k,v in picardSorted:
    print(k,"\t",v, end=", ")
file.close();
