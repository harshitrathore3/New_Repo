'''x=int(input("Enter todays date"))
print("No. of days left are",30-x)
Another smart way of this is
'''
d,m,y = map(int,input("Enter Date in DD MM YYYY form : ").split())
mon = {1:30,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
print("Days Left : ",mon[m]-d)
