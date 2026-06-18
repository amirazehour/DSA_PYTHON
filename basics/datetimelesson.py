import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))#RETURN THE DAY

#Creating a date object
x = datetime.datetime(2004,6,1)

#date directive
print(x.strftime("%A")) # long week day name
print(x.strftime("%a")) # short week day name
print(x.strftime("%B")) #or b month name
print(x.strftime("%C")) #centry
print(x.strftime("%y")) # year short version exmp 26
print(x.strftime("%d")) #or D day of the month
print(x.strftime("%m")) #month number
print(x.strftime("%w")) #weekday number
print(x.strftime("%H")) #hour 0-23
print(x.strftime("%I")) #hour 0-12
print(x.strftime("%p")) #pm/am
"""
M minutes
S seconds 
f milsec
z utc offset (+0100)
Z time zode
j day number of the year
U week number sunday as first
W same monday 1st
"""
