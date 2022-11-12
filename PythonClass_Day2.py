#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World!!!")


# In[2]:


money = True
if money == True :
    print("택시를 타자")
else :
    print("걸어 가자")


# In[6]:


money = 3000

if money >= 5000:
    print("택시를 타자")
elif money >= 1000:
    print("버스를 타자")
else:
    print("걸어 가자")
    


# In[12]:


# 학생의 성적을 입력 받아서
# 점수가 90 이상이면 "A 학점입니다"
# 점수가 80 이상이면 "B 학점입니다"
# 점수가 70 이상이면 "C 학점입니다"
# 점수가 60 이상이면 "D 학점입니다"
# 나머지는 모두 "F 학점입니다"

score = int(input("학생의 점수는 몇 점입니까?"))

if score >= 90:
    print("A 학점입니다")
    
elif score >= 80:
    print("B 학점입니다")
    
elif score >= 70:
    print("C 학점입니다")
    
elif score >= 60:
    print("D 학점입니다")
    
else:
    print("F 학점입니다")


# In[13]:


# while

no = 10

while no >= 0 :
    print(no)
    no = no -1
    


# In[16]:


prompt = "1.덧셈 / 2.뺄셈 / 3.곱셈 / 4.나눗셈 / 5.종료"
no = 0

while no <= 4:
    print(prompt)
    no = int(input())
    


# In[21]:


# while 문의 경우에는 반복 횟수가 정확하지 않을 경우가 많기 때문에 조건에서 뿐만이 아니라 중간에 반복을 종료 시키는 방법 도 필요하다. 

no = 0

while no <= 15 :
    print(no)
    no = no + 1
    


# In[22]:


no = 0

while True :
    print(no)
    no = no + 1
    
    if no > 10 :
        break
        
    


# In[33]:


no = 1
sum = 0

while no < 100 :
    if no%3 == 0 :
        sum = sum + no
        no = no + 1

    else :
        no = no + 1
    
print("1부터 100 까지 3의 배수의 합은", sum)


# In[35]:


no = 1
sum = 0

while no < 100 :
    if no%3 == 0 :
        sum = sum + no
        
    no = no + 1  # no += 1
    
print("1부터 100 까지 3의 배수의 합은", sum)


# In[42]:


for i in [1,2,3,4,5,6,7,8,9, 10] :
    print(i)


# In[45]:


math = [80,90,70, 70, 100]

j = 1
for i in math :
    if i>= 90 :
        print(j, "번째 학생은 합격입니다.")
    else :
        print(j, "번째 학생은 불합격입니다.")
    j += 1


# In[58]:


for i in [1,2,3,4,5,6,7,8,9,10] :
    if i%2 == 0:
        
        print(i)
    


# In[59]:


for i in [1,2,3,4,5,6,7,8,9,10] :
    if i%2 != 0:
        continue
        
    print(i)
    


# In[61]:


for i in range(10) :
    if i%2 == 0: 
        print(i)
    


# In[62]:


for i in range(1,11):    # 두번쩨 수는 미만
    print(i)
    


# In[66]:


# for 문으로 구구단 표현하기

for i in range(2,10):   # i 는 단을 표헌
    for j in range(1,10):  # j 는 곱하는 수를 표현
        print(i,"*",j,"=",i*j,end="\t")
    print()
        


# In[73]:


# for 문으로 구구단 표현하기

for i in range(1,10):   # i 는 단을 표헌
    for j in range(2,10):  # j 는 곱하는 수를 표현
        print(j,"*",i,"=",j*i,end="\t")
    print()


# In[76]:


# range 를 사용, 100 이하의 수중 짝수의 합을 구하시오

sum = 0
for i in range(101):
    if i%2 == 0:
        sum += i
print(sum)


# In[80]:


sum = 0
for i in range(0,101,2):
     sum += i
print(sum)


# In[86]:


# 리스트 축약/내포  List Comprehension
# 리스트를 보다 편리하고 직관적으로 만드는 방업이다

list1 = [1,2,3,4,5]
print("list1 = ",list1)

list2 = [num for num in list1]
print("list2 = ",list2)

list3 = [num*2 for num in list1]
print("list3 = ",list3)

list4 = [num for num in list1 if num%2==0]
print("list4 = ",list4)


# In[87]:


no = int(input("점수는?"))

if no >= 80 :
    print("합격입니다")
else :
    print("불합격입니다")


# In[91]:


no = int(input("점수는?"))

print("합격입니다" if no >=80 else "불합격입니다")

