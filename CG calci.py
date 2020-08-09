credits={1:23,2:47,3:68,4:93,5:116,6:139,7:163}

curcg=float(input("Enter your current CGPA: "))
cursem=int(input("No. of completed sems: "))
curcre=int(credits[cursem])
    
score=round((curcg*curcre))
gpa=float(input("Expected GPA of current sem: "))
cre=int(credits[cursem+1]-credits[cursem])
curscore=round((gpa*cre))
totscore=score+curscore
totcre=curcre+cre
newcg=totscore/totcre
print("Your expected CGPA:%.2f"%(newcg))    
               
