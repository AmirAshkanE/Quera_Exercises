
# init_input=input()
def calculator(n,m,li):
    n,m,li=n,m,li
    sep_list=[]

    i_count=0
    m_count=0
    s=0
    for i in li:
        s+=i
        i_count+=1
        if i_count>=m:
            sep_list.append(s)
            s=0
            i_count=0
            m_count+=1
        
        if (m_count+1)*m>len(li):
            m=len(li)-(m_count*m)
        
    result=0
    b=0
    while b <len(sep_list):
        if b % 2==0:
            result+=sep_list[b]
        else:
            result-=sep_list[b]
        b+=1
    return result

# Check with the teacher
