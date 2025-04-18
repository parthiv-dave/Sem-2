import pandas as pd

dt1 = pd.Timestamp('2012-01-15')

dt2 = pd.Timestamp('2012-01-15 21:20')

dt3 = pd.Timestamp.now()

dt4 = pd.Timestamp.today().normalize()

dt5 = pd.Timestamp.today().date()

dt6 = dt3.time()

dt7 = pd.Timestamp.now().time()

print("a) Date time object for Jan 15, 2012:", dt1)
print("b) Specific date and time of 9:20 pm:", dt2)
print("c) Local date and time:", dt3)
print("d) A date without time:", dt4)
print("e) Current date:", dt5)
print("f) Time from a date time:", dt6)
print("g) Current local time:", dt7)
