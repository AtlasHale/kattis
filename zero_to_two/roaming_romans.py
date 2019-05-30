miles = float(input())
roman_miles = 1000*(miles*5280)/4854
if(roman_miles - int(roman_miles) < .5):
    print(int(roman_miles))
else:
    print(int(roman_miles+1))
