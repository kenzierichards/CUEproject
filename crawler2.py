#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:20:10 2021

@author: emilymitchell
"""

import requests 
import re
import csv
import xlwt
from xlwt import Workbook

def main():
       
    wb = xlwt.Workbook(encoding="utf-8")
  

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
            event = re.split(r'Girls|Boys[\s\S]*?Girls|Boys', string) #event has all information
            
    
        #get event name and just event results
        eventName = []
        eventBodyList = []
        visitedEvents = []
        for i in range (1, len(event)):
            #get name of event
            eventNameList = event[i].split("\n") #event name list steps through each event
            #print(eventNameList)
            if "4x" not in eventNameList[0] and "(" not in eventNameList[0] and eventNameList[0] not in visited: #removes relays
                #then append it to event name and add to body list
                eventName.append(eventNameList[0]) #event name has names of all events
                visitedEvents.append(eventNameList[0])
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
                    #only keep finals data for simplicity
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
    
                    finalMark = finalMark.replace("#", "")
                    finalMark = finalMark.replace("*", "")
                    finalMark = finalMark.replace("J", "") 
                    #create list of current entry
                    entry = [athleteName, meetName, eName, place, grade, school, finalMark] 
                    #append entry to rows
                    rows.append(entry) 
                
                #pass non-needed info
                except: 
                    pass #pass when place not given
    
        writeToCSV(rows, meetName)
        writeToExcel(wb, rows, meetName)


def writeToCSV(rows, meetName):
    #column headers for csv
    csvFields = ["Name", "Meet", "Event", "Place", "Grade", "School", "Mark"]  
    #write data to csv file
    with open(meetName + '.csv', 'w') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(csvFields)
        csvWriter.writerows(rows)
        csvFile.close()
      
#method to write to excel file
def writeToExcel(wb, rows, meetName): 
    #create new sheet
    sheet = wb.add_sheet(meetName)
    #add headers
    sheet.write(0, 0, "Name")
    sheet.write(0, 1, "Meet")
    sheet.write(0, 2, "Event")
    sheet.write(0, 3, "Place")
    sheet.write(0, 4, "Grade")
    sheet.write(0, 5, "School")
    sheet.write(0, 6, "Mark")
    
    #loops to write rows
    r = 1
    c = 0 
    #for all entries in rows list
    for i in rows:
        #for each column
        for j in range(0,7):
            #write data
            sheet.write(r, c, i[j])
            #increase column
            c = c + 1
        #reset columm
        c = 0
        #increase row
        r = r + 1

    #save workbook
    wb.save("meetData.xls")
    
main()