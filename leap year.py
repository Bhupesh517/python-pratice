("year 2024 is a leap year are not a leap year")
year = int(input("year: "))
if (year%4 == 0) :
    if(year % 100 != 0) or (year % 400 == 0) :
     print ("it's leap year ")
    else:
       print ("not a leap year ")

else :
    print ("not a leap year ")