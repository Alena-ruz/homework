n=int(input())
dist=1
way=1
for i in range(2,n+1):
    dist1=1/i
    dist=dist+dist1*(-1)**(i+1)
    way=way+dist1
    continue
print("Расстояние до дома, км: "+ str(round(dist,1)))
print("Всего пройдено, км: "+str(round(way,1)))