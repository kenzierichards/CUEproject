#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:20:10 2021

@author: emilymitchell
"""

import requests 
import re
import csv

def main():
    
    #focus on CT state meets for past x years
    #get to track and field page
    #get to meet results page
    #just need events results tab
    #save event title
    #pull get relevant info
    
    
    #r = requests.get("http://ciacsports.com/site/") #home page 
    #r = requests.get("http://ciacsports.com/site/?page_id=972") #outdoor tf
    #r = requests.get("http://ciacsports.com/site/?page_id=970") #indoor tf
    #r = requests.get("https://content.ciacsports.com/ot19o.shtml") #outdoor track 19 open 

  '''  
    stak = list()
    visited = list()
    stak.append("http://ciacsports.com/site")
    visited.append("http://ciacsports.com/site")
    
    link = stak.pop()
    r = requests.get(link)
    html = r.text
    
    outdoorTF = re.findall(r'href="(.*)?".*Outdoor Track', html)
    print(outdoorTF)
    for url in outdoorTF:
        if url not in visited:
            stak.append(url)
            visited.append(url)
   #indoorTF = re.findall(r'href="(.*)?".*Indoor Track', html)
   #print(indoorTF)
   #for url in indoorTF:
       #if url not in visited:
           #stak.append(url)
           #visited.append(url)
    
    link = stak.pop()
    r = requests.get(link)
    html = r.text
      
    for x in range(19,20):# year range of results
        year = str(x)
        results = re.findall(r'href="(https://content.ciacsports.com/.*'+year+'.*html)"', html) 
        #print(results)
        for url in results:
            if url not in visited:
                stak.append(url)
                visited.append(url)
        print(stak) #now stak has all links to results for desired year
        
        
    #for each meet, get relevant data, write it to text file
    #by event?
    #by athlete?
    
'''
    
#r = requests.get("http://ciacsports.com/site/?page_id=972")
#html = r.text
#meetResults = re.findall(r'href="(https://content.ciacsports.com/.*19.*html)"', html) #all '19 results
#print(meetResults)
r2 = requests.get("https://content.ciacsports.com/ot19o.shtml")
html2 = r2.text
#get only event results
eventResults = re.findall(r'Event Results[\s\S]*<pre>[\s\S]*?Performance List', html2) 

#get meet name
title = re.findall(r'<title>([\s\S]*)?</title>', html2)
meetName = ""
for element in title:
    meetName += element


#split by event
for string in eventResults:
    event = re.split(r'Girls|Boys[\s\S]*?Girls|Boys', string) #event has all information


#can I add girls and boys to event name PLEASE

#get event name and just event results
eventName = []
eventBodyList = []
for i in range (1, len(event)):
    #get name of event
    eventNameList = event[i].split("\n") #event name list steps through each event
    #print(eventNameList)
    if "4x" not in eventNameList[0]: #removes relays
       #then append it to event name and add to body list
        eventName.append(eventNameList[0]) #event name has names of all events
        #get list of event
        eventBodyList += re.findall(r'(1 [\s\S]*)', event[i]) #event body list has all event information in list format

#add girls label to first half of event and boys label to second half
for i in range(0, len(eventName)):
    if i < len(eventName)/2:
        eventName[i] = "Girls" + eventName[i]
    else:
        eventName[i] = "Boys" + eventName[i]
 
#create meet list
meet = [[[]] for i in range(len(eventBodyList))]

#add event and person to meet list
for i in range (0, len(eventBodyList)):
    newList = ""
    newList += eventBodyList[i]
    person = newList.splitlines()
    meet[i] = person

#create row list for csv file
rows = []

#get relevant info
for i in range(0, len(eventBodyList)): #len(eventBodyList)
    for j in range(0, len(meet[i])): #len(meet[i])
        #split by spaces then get rid of empty strings
        text = meet[i][j].split(" ")
        finalText = [x for x in text if x.strip()]
        #print(finalText)
        #get rid of extra stuff
        try:
            place = int(finalText[0]) #get place 
            eName = eventName[i] #get event name
            eNameNext = eventName[i+1] #get next event name
            if eName == eNameNext:
                break
            #athlete has two names
            if finalText[3].startswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
                athleteName = finalText[1] + " " + finalText[2]
                grade = int(finalText[3]) #get grade year
                #if school is one word
                if finalText[5].startswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")): 
                    school = finalText[4]
                    finalMark = finalText[6]
                #if school is two words
                else:
                    school = finalText[4] + " " + finalText[5] 
                    finalMark = finalText[7]
            #if athlete has three names
            else:
                athleteName = finalText[1] + " " + finalText[2] + " " + finalText[3] 
                grade = int(finalText[4]) #get grade year
                #if school is one word
                if finalText[6].startswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")): 
                    school = finalText[5]
                    finalMark = finalText[7]
                #if school is two words
                else:
                    school = finalText[5] + " " + finalText[6] 
                    finalMark = finalText[8]

            #create list of current entry
            entry = [athleteName, meetName, eName, place, grade, school, finalMark] 
            #append entry to rows
            rows.append(entry) 
            
        #pass non-needed info
        except: 
            pass #pass when place not given

#column headers for csv
csvFields = ["Name", "Meet", "Event", "Place", "Grade", "School", "Mark"]  
#write data to csv file
with open('athleteData.csv', 'w') as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(csvFields)
    csvWriter.writerows(rows)

  
main()