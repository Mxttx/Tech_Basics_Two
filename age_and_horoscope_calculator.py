from datetime import datetime
from datetime import date
import.os
os.system("clear")

def calculate_age(dob):
    day = int(input ("What is the day of your birthday?"))
    month = int(input ("What is the month of your birthday?"))
    birthdate_input = int(input("What is the year of your birthday?"))

    dob = input("What is your date of birth? Please specify in the format YYY-MM-DD")
    year, month, day = dob.split("-")
    year = int(year)
    month = int(month)
    day = int(day)
    dob = date(year, month, day)

    current_date = date.today()
    age = (int(current_date - dob).days/365.25)
    return(age)

def calculate_horoscope(month, day):
    if 
