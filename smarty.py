import sys
sys.path.append('/module/')
import module
from module.mathy import *
print(strings[0])
print(strings[1])
while True:
    print()
    text=input("Enter some text")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_num_from_txt(text)
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except:
                print("Something is wrong,Please retry")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()
        print(l)
            
