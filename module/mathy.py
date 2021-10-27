strings=["Welcome to smart calculator","My name is Smarty",
         "Thanks","Sorry,This is beyond my abilities."]
def extract_num_from_txt(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return (l) 
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        h-=1
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def myname():
    print(strings[1])
def end():
    print(strings[2])
    input("Press any key to exit")
    exit()
def sorry():
    print(strings[3])

operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"SUBSTRACT":substract,"DIFERENCE":substract
            ,"SUBSTRACTION":substract,"MINUS":substract,"MULTIPLY":multiply,"PRODUCT":multiply,
            "MULTIPLICATION":multiply,"DIVISION":divide,"DIVIDE":divide,"LCM":lcm,"HCF":hcf}
commands={"NAME":myname,"EXIT":end,"END":end,"CLOSE":end}
    
    
    
