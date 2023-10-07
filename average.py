total=0
count=0
while True:
    inp=input("enter the numnber =")
    if inp=='done':
        break
    value=float(inp)
    total=total+value
    count=count+1
print("total = " ,total)
print("average = ",total/count)
