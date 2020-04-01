query=input()    
list=[i for i in input().split()]    
answer=[]
for i in list:
 if (i[:len(query)]==query):
  answer.append(i)
print(answer)    
    
