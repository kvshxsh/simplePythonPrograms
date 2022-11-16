num = 1
count0 = 0
sum0 = 0
sum1 = 0
cont = 'y' or 'Y'
while((cont=='y') or (cont=='Y')):
    n = int(input("Input num %d: " %(num)))
    num=num+1
    if(n%2==0):
        count0=count0+1
        sum0=sum0+n
    elif(n%2==1):
        count0 =count0+1
        sum1=sum1+n
    cont =input("Do you wish to continue? (Y/N)")
print(f"List of even numbers:{count0}")
print(f"Sum of all the even numbers:{sum0}")
print(f"List of odd numbers:{count0}")
print(f"Sum of all the odd numbers:{sum1}")