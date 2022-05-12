import datetime


cur_date = datetime.date.today()


pre = []
present = []
day_order = input("Day Order: ")
period = input("Period: ")
hr = input("Hour: ")
i = 1

while i>0:
        if (i>0):
                i = int(input("Roll No: "))
                pre.append(i)
                continue
        else:
                break
print()

print("III BSC CS A")
print("Date: ", cur_date)
print("Day Order: ",day_order)
print("Hour: ",hr)
print("Period : ",period)

for i in pre:
        if i not in present:
                present.append(i)
present.sort()
#remove 0
print("Present : " + str(len(present)))
print("Absent: " + str(60-len(present)))
print(present)
