

import pandas as pd
import numpy as np
member_list1 = []
trophy_list1 = []
member_list2 = []
trophy_list2 = []
member_list3 = []
trophy_list3 = []

number_of_members = int(input("How many members are in the club?"))
for i in range(number_of_members):
    member = input("enter a member")
    member_list1.append(member)
    trophies = int(input("enter in the member's trophies"))
    trophy_list1.append(trophies)
    
number_of_members2 = int(input("How many members are in the club?"))

for i in range(number_of_members2):
    member = input("enter a member")
    member_list2.append(member)
    trophies = int(input("enter in the member's trophies"))
    trophy_list2.append(trophies)

number_of_members3= int(input("How many members are in the club?"))

for i in range(number_of_members3):
    member = input("enter a member")
    member_list3.append(member)
    trophies = int(input("enter in the member's trophies"))
    trophy_list3.append(trophies)

    
Eternal = {"Players" : member_list1,
        "trophies": trophy_list1
        
        }
Eternal_Flames = {"Players" : member_list2,
            "trophies" : trophy_list2
            }
Eternal_Aura = {"Players" : member_list3,
            "trophies" : trophy_list3
    
            }

Eternal1 = pd.DataFrame(Eternal)
Eternal2 = pd.DataFrame(Eternal_Flames)
Eternal3 = pd.DataFrame(Eternal_Aura)
combined = pd.merge(Eternal1,Eternal2, on = "trophies", how = "outer")
EternalCombined = pd.merge(combined, Eternal3, on = "trophies", how = "outer")
print(EternalCombined.describe())
