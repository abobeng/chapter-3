hour = int(input("Enter hour between 1-12 : "))
newh = int(input("How many hours ahead : "))

x = hour + newh

if x > 12:
    x -= 12

print("Time at that time would be : ", x, "o'clock")