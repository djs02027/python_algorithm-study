def solution(new_id):
    step1=new_id.lower()
    step2=[]
    for s in step1:
        if s.islower()==True or s.isdigit()==True or s=='-' or s=='_' or s=='.':
            step2.append(s)       
    flag=0
    step3=[]
    
    for s in step2:
        if flag==0 and s=='.':
            flag=1
            step3.append('.')
        elif s!='.':
            flag=0
            step3.append(s)
            
      
    if step3[0]=='.' and step3[-1]=='.':
        step3=step3[1:]
        step3=step3[:-1]
    elif step3[0]=='.':
        step3=step3[1:]
    elif step3[-1]=='.':
        step3=step3[:-1]
        
    if not step3:
        step3.append('a')
    if len(step3)>=16:
        step3=step3[0:15]
        if step3[-1]=='.':
            step3=step3[:-1]
    # print(help(list))
    if len(step3)<=2:
        while len(step3)!=3:
            step3.append(step3[-1])
                
    answer = ''.join(map(str,step3))
    return answer