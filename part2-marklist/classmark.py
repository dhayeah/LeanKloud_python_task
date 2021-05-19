import sys
import pandas as pd
from csv import reader


first_arg = sys.argv[1]
df = pd.read_csv (first_arg)
maths=biology=english=physics=chem=hindi=0
marks={
    "maths": 0,
    "biology": 0,
    "english": 0,
    "physics":0,
    "chem":0,
    "hindi":0,
    "one":0,
    "two":0,
    "three":0
    }
topper={
    "maths":'',
    "biology":'',
    "english":'',
    "physics":'',
    "chem":'',
    "hindi":'',
    "one":'',
    "two":'',
    "three":''
    
    }

num=0


with open(first_arg, 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    if header != None:
        for row in csv_reader:
            maths=int(row[1])
            biology=int(row[2])
            english=int(row[3])
            physics=int(row[4])
            chem=int(row[5])
            hindi=int(row[6])

            
            if(maths > int(marks["maths"])):
                marks["maths"]=row[1]
                topper["maths"]=row[0]
            if(biology > int(marks["biology"])):
                marks["biology"]=row[2]
                topper["biology"]=row[0]
            if(english > int(marks["english"])):
                marks["english"]=row[3]
                topper["english"]=row[0]
            if(physics > int(marks["physics"])):
                marks["physics"]=row[4]
                topper["physics"]=row[0]
            if(chem > int(marks["chem"])):
                marks["chem"]=row[5]
                topper["chem"]=row[0]
            if(hindi > int(marks["hindi"])):
                marks["hindi"]=row[6]
                topper["hindi"]=row[0]

            num=(maths+biology+english+physics+chem+hindi)

            if(num > marks["one"]):
                marks["three"],topper["three"]=marks["two"],topper["two"]
                marks["two"],topper["two"]=marks["one"],marks["one"]
                
                marks["one"]=num
                topper["one"]=row[0]
            elif(num > marks["two"]):
                marks["three"],topper["three"]=marks["two"],topper["two"]
                marks["two"]=num
                topper["two"]=row[0]
            elif(num > marks["three"]):
                marks["three"]=num
                topper["three"]=row[0]

print('Topper in Maths is ' +topper["maths"])
print('Topper in Biology is ' +topper["biology"])
print('Topper in English is ' +topper["english"])
print('Topper in Physics is ' +topper["physics"] )
print('Topper in Chemistry is '+topper["chem"])
print('Topper in Hindi is '+topper["hindi"])

print('Best students in the class are '+topper["one"]+','+topper["two"]+','+topper["three"])

print("-------------------------")
print("Time complexity => O(n)")


r"""
OUTPUT :

(env) C:\Users\Dhayanidhi\Desktop\part2>py tip.py Student_marks_list.csv
Topper in Maths is Manasa
Topper in Biology is Sreeja
Topper in English is Praneeta
Topper in Physics is Sagar
Topper in Chemistry is Manasa
Topper in Hindi is Aravind
Best students in the class are Manodhar,Bhavana,Sourav
Time taken--- 0.0025200843811035156 seconds ---
Time complexity => O(n)

"""
