spl_char = 0
num = 0
up_case = 0
low_case = 0
count = 'y' or 'Y'
while((count=='y') or (count=='Y')):
    char = input("Enter character:")
    if((char>='a') or (char<='z')):
        low_case = low_case+1
    elif((char>='A') or (char<='Z')):
        up_case = up_case+1
    elif((char>='0') or (char<='9')):
        num = num + 1
    else: 
        spl_char = spl_char+1
    count= input("y to continue/Any other key to stop.")
print("Number of entered lowercase alphabets: %s" %(low_case))
print("Number of entered uppercase alphabets: %s" %(up_case))
print("Number of entered integers: %d" %(num))
print("Number of entered special characters: %s" %(spl_char))