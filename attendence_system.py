first =[]
second =[]
third =[]
fourth =[]
fifth =[]
sixth =[]
seventh =[]
eighth =[]
nineth =[]
tenth =[]
eleventh =[]
twelveth =[] 

while True :
    a=input("enter class for attendence :")
    
    if a=="1" :
        b=int(input("Enter total number of student :"))    
        for i in range(b): 
            c=int(input("Enter roll no. of student :"))
            first.append(c)
        print("Present student are ",first)
    
    elif a=="2" :
        b=int(input("Enter total number of student :"))
        for i in range(b): 
            c=int(input("Enter roll no. of student :"))
            second.append(c)
        print("Present students are ",second)
                
    elif a=="3" :
        b=int(input("Enter total number of student :"))
        for i in range(b): 
            c=int(input("Enter roll no. of student :"))
            third.append(c)
        print("Presents students are ",third)
            
    elif a=="4" :
        b=int(input("Enter total number of student :"))
        for i in range(b): 
            c=int(input("Enter roll no. of student :"))
            fourth.append(c)
        print("Present students are ",fourth)
    
    elif a=="5" :
        b=int(input("Enter total number of student :"))
        for i in range(b): 
            c=int(input("Enter roll no. of student :"))
            fifth.append(c)       
        print("Present students are ",fifth)     
            
    elif a=="6" :
        b=int(input("Enter total number of student :"))
        for i in range(b): 
            c=int(input("Enter roll no. of student :"))
            sixth.append(c)
        print("Present student are ",sixth)         
            
    elif a=="7" :
        b=int(input("Enter total number of student :"))
        for i in range(b): 
            c=int(input("Enter roll no. of student :"))
            seventh.append(c) 
        print("Present students are ",seventh)
            
    elif a=="8" :
        b=int(input("Enter total number of student :"))
        for i in range(b): 
            c=int(input("Enter roll no. of student :"))
            eighth.append(c)    
        print("present students are ",eighth)    
            
    elif a=="9" :
        b=int(input("Enter total number of student :"))
        for i in range(b): 
            c=int(input("Enter roll no. of student :"))
            nineth.append(c)
        print("Present students are ",nineth)
            
    elif a=="10":
        b=int(input("Enter total number of student :"))
        for i in range(b): 
            c=int(input("Enter roll no. of student :"))
            tenth.append(c)
        print("Present students are ",tenth)
            
    elif a=="11" :
        b=int(input("Enter total number of student :"))
        for i in range(b): 
            c=int(input("Enter roll no. of student :"))
            eleventh.append(c)
        print("Present students are",eleventh)
            
    elif a=="12" :
        b=int(input("Enter total number of student :"))
        for i in range(b): 
            c=int(input("Enter roll no. of student :"))
            twelveth.append(c)
        print("Present students are",twelveth)
            
    elif a=="all students" :
        print("class 1st",first)
        print("class 2nd",second)
        print("class 3rd",third)
        print("class 4th",fourth)
        print("class 5th",fifth)
        print("class 6th",sixth)
        print("class 7th",seventh)
        print("class 8th",eighth)
        print("class 9th",nineth)
        print("class 10th",tenth)
        print("class 11th",eleventh)
        print("class 12th",twelveth)

        b=len(first+second+third+fourth+fifth+sixth+seventh+eighth+nineth+tenth+eleventh+twelveth)
        print(f"Total {b} students are present")
    
    elif a=="done" :
        break
    
    else :
        print("Please choose correct class")
        
b=len(first+second+third+fourth+fifth+sixth+seventh+eighth+nineth+tenth+eleventh+twelveth)
print(f"Today {b} students are present")