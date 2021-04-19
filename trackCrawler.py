#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:47:02 2021

@author: emilymitchell
"""

import requests 
import re
import csv

def main():
       
    #column headers for csv
    csvFields = ["Name", "Meet", "Event", "Place", "Grade", "School", "Mark"]  
    #write data to csv file
    with open('trackData.csv', 'w') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(csvFields)
        csvFile.close()

    #create stack and visited lists
    stak = list()
    visited = list()
    stak.append("http://ciacsports.com/site") #home site
    visited.append("http://ciacsports.com/site")
    
    #get first html
    link = stak.pop()
    r = requests.get(link)
    html = r.text
    
    #find outdoor TF page
    outdoorTF = re.findall(r'href="(.*)?".*Outdoor Track', html)
    #get url and append to stak and visited
    for url in outdoorTF:
        if url not in visited:
            stak.append(url)
            visited.append(url)
     

    #find indoor TF home page
    indoorTF = re.findall(r'href="(.*)?".*Indoor Track', html)
    #get url and append to stak ad visited 
    for url in indoorTF:
       if url not in visited:
           stak.append(url)
           visited.append(url)
   
    #create new stack and visited to hold results links
    stakResult = list()
    visitedResult = list()
    
    #pop everything in stak
    while stak:
         link = stak.pop()
         r = requests.get(link)
         html = r.text
         #range of years you want results from 
         for x in range(19,20): #testing with just 2019
            year = str(x)
            #get all relevant links
            results = re.findall(r'href="(https://content.ciacsports.com/.*'+year+'[^dh].*html)"', html) 
            #get url and append to new stak and visited
            for url in results:
                if url not in visitedResult:
                    stakResult.append(url)
                    visitedResult.append(url)
    #print(stakResult) #now stak has all links to results for desired year
        

    while stakResult: 
        link = stakResult.pop()
        #print(link)
        r = requests.get(link)
        html = r.text
            
    
        eventResults = re.findall(r'Event Results[\s\S]*<pre>[\s\S]*', html)
        
    
        #get meet name
        title = re.findall(r'<title>([\s\S]*)?</title>', html)
        meetName = ""
        for element in title:
            meetName += element
    

        #split by event
        for string in eventResults:
            event = re.split(r'(?=Girls)|(?=Boys)|(?=Women)|(?=Men)', string) #event has all information
            

        #get event name and just event results
        eventName = []
        finalEventName = []
        eventBodyList = []
        finalEventBody = []
        visitedEvent = []

        
        for i in range (1, len(event)):
            #get name of event
            eventNameList = event[i].split("\n") #event name list steps through every line in each event
            if "4x" not in eventNameList[0] and "(" not in eventNameList[0] and "<" not in eventNameList[0] and "Prelims" not in eventNameList[0] and "Dev" not in eventNameList[0]:
                if "Boys " in eventNameList[0] or "Girls " in eventNameList[0]:
                    eventName.append(eventNameList[0])
                    eventBodyList += re.findall(r'(1 [\s\S]*)', event[i])

 
        for j in range(0, len(eventName)):
            try:
                if(eventName[j] == eventName[j+1]):
                    pass
                else:
                    if eventName[j] in visitedEvent:
                        pass
                    else:
                        visitedEvent.append(eventName[j])
                        finalEventName.append(eventName[j])
                        finalEventBody.append(eventBodyList[j])
            except:
                pass

        #create meet list
        meet = [[[]] for i in range(len(finalEventBody))]
    
        #add event and person to meet list
        for i in range (0, len(finalEventBody)):
            newList = ""
            newList += finalEventBody[i]
            person = newList.splitlines()
            meet[i] = person
    
        #create row list for csv file
        rows = []
    
        
        #get relevant info
        for i in range(0, len(finalEventBody)): 
            for j in range(0, len(meet[i])): 
                #split by spaces then get rid of empty strings
                text = meet[i][j].split(" ")
                finalText = [x for x in text if x.strip()]
                
                #get rid of extra stuff
                try:
                    place = int(finalText[0]) #get place 
                    eName = visitedEvent[i] #get event name
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
    
                    finalMark = finalMark.replace("#", "")
                    finalMark = finalMark.replace("*", "")
                    finalMark = finalMark.replace("J", "") 
                    finalMark = convertToInt(finalMark)
                    #create list of current entry
                    entry = [athleteName, meetName, eName, place, grade, school, finalMark] 
                    #append entry to rows
                    rows.append(entry) 
                
                #pass non-needed info
                except: 
                    pass #pass when place not given
                    
        writeToCSV(rows, meetName)
        #writeToExcel(wb, rows, meetName)

def convertToInt(finalMark):
    try:
        return float(finalMark)
    except:
        if ":" in finalMark:
            time = finalMark.split(":")
            minute = float(time[0])
            seconds = minute * 60
            finalMark = seconds + float(time[1])
            return finalMark
        
        elif "-" in finalMark:
            length = finalMark.split("-")
            feet = float(length[0])
            inches = feet * 12
            finalMark = inches + float(length[1])
            return finalMark
        

def writeToCSV(rows, meetName):
    #column headers for csv
    #csvFields = ["Name", "Meet", "Event", "Place", "Grade", "School", "Mark"]  
    #write data to csv file
    with open('trackData.csv', 'a') as csvFile:
        csvWriter = csv.writer(csvFile)
        #csvWriter.writerow(csvFields)
        csvWriter.writerows(rows)
        csvFile.close()
      
main()