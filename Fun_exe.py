#Example Script

def divisibility(number):
    if number % 15 == 0:
        print ('An Awesome Wave')
    elif number % 5 == 0:
        print ('Wave')
    elif number % 3 == 0:
        print ('Awesome')
    else:
        print number


# In[2]:

for number in range (1,101,1):
    divisibility(number)


# In[ ]:



