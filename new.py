'''email = input("Enter an Email ID : ")
gmail = '@gmail.com' in email
yahoo = '@yahoo.com' in email
hotmail = '@hotmail.com' in email
if(gmail==True or yahoo==True or hotmail==True):
    print("Valid Email ID")
else:
    print("Not a valid Mail ID")
print(ord('A'))

phone = input("Enter the Phone Number : ")
if((len(phone)==12) and phone[3]=='-' and phone[7]=='-'):
    print("Valid Phone Number")
else:
    print("Not a Valid Phone Number")'''

str1="PANDA"
str2="Python"
if(str1>str2):
    big=str1
    small=str2
else:
    big=str2
    small=str1
print(small)
a=0
z=0
length=len(big)
x=length-2
print(x)
l1 = int(-(len(big)/2)-1)
for b in range(-1,l1,-1):
    print(" "*z,big[a]," "*x,big[b]," "*z)
    a+=1
    x-=2
    z+=1



