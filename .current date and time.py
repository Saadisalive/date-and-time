from datetime import date , time , datetime

#calling the today
#function of date class
today = date.today()
now = datetime.now()
print("\nCurrent Date is", today)
("\nCurrent DAte and time is ",now)

#printing date cpomponents
print("\nDate components",today.year,today.month, today.day)