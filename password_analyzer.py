p=input("Enter Password:")
x=len(p)
pl=p.lower()
CP={# classic
    "password", "passw0rd", "pass", "passcode", "admin", "administrator",
    "root", "user", "guest", "test", "demo", "login", "welcome", "letmein",
    "secret", "master", "changeme", "default", "access", "system",
    # affection / emotion
    "iloveyou", "loveyou", "love", "sunshine", "princess", "angel",
    "baby", "honey", "sweety", "lovely", "darling", "freedom",
    # animals / fun
    "monkey", "dragon", "tiger", "shadow", "ninja", "batman", "superman",
    "hunter", "killer", "master", "soccer", "football", "cricket",
    "hello", "freedom", "whatever", "trustno1", "starwars",
    # India / Kerala context
    "india", "kerala", "krishna", "ganesh", "shiva", "sai", "ram",
    "mumbai", "delhi", "chennai", "bangalore", "thrissur",
    # tech
    "computer", "internet", "google", "facebook", "whatsapp", "instagram",
    "windows", "linux", "python", "mypassword", "newpassword",
    #repeated words
    "passwordpassword", "adminadmin", "testtest", "useruser",
    "abcabc", "abcabcabc", "123123", "123123123", "112233", "445566",
    "121212", "696969", "159159", "147147",
    "aaaaaa", "aaaaaaaa", "zzzzzz",
    #sequence
    "abcdefghijklmnopqrstuvwxyz",
    "zyxwvutsrqponmlkjihgfedcba",
    "0123456789",
    "9876543210",
    "abcdef", "abcd", "abc", "xyz", "cba",
    #keyboard patterns
    # rows
    "qwertyuiop", "qwerty", "qwert", "asdfghjkl", "asdfgh", "asdf",
    "zxcvbnm", "zxcvbn", "zxcv",
}
f=1
lg=0
u=0
l=0
d=0
s=0
points=0
if(pl in CP):
    print("Password is too common")
    f=0
if (x>=8 and x<=20):
   lg=1 
   points+=10
for i in p:
   if(i.isupper()):
      u=1
      points+=10
   if(i.islower()):
      l=1
      points+=10
   if(i.isdigit()):
      d=1
      points+=10
   if(i in ['!','@','#','$','%','^','&','*','(',')','-','=','_','+']):
      s=1
      points+=10
if(lg==0):
   print("password length to be between 8 and 20")
if(u==0):
   print("Missing Atleast one uppercase letter")
if(l==0):
   print("Missing Atleast one lowercase letter")
if(d==0):
   print("Missing Atleast one digit")
if(s==0):
   print("Missing Atleast one special character from !,@,#,$,%,^,&,*,(,),-,=,+,_")
if(f==1 and lg==1 and u==1 and l==1 and d==1 and s==1):
   print("Password is strong")
   print("points scored=", points)
