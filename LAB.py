#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("파일 과제")
read_file = open("score.txt", "r")
write_file = open("report.txt", "w")

while True:
    l = read_file.readline().rstrip()
    if l == '':
           break
        
    l_list = l.split()
    midterm = l_list[1]
    finalterm = l_list[2] 
    um = float(midterm) * 0.4 + float(finalterm) * 0.6
    
    grade = ''
    if um >= 90:
        rade = 'A'
    elif um >= 80:
        rade = 'B'
    elif um >= 70:
        rade = 'C'
    elif um >= 60:
        rade = 'D'
    else:
        rade = 'F'
        
    data= "%.1f(%s)" %(um, rade)
    write_file.write(l+" "+data+"\n")
read_file.close()


# In[ ]:




