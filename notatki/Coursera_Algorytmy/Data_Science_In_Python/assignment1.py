# In[2]:


def example_word_count():
    # This example question requires counting words in the example_string below.
    example_string = "Amy is 5 years old"

    # YOUR CODE HERE.
    # You should write your solution here, and return your result, you can comment out or delete the
    # NotImplementedError below.
    result = example_string.split(" ")
    return result

    #raise NotImplementedError()

example_word_count()

# In[5]:


import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    my_list = simple_string.split()
    names1= [char for char in my_list if char[0].isupper()]
    names1 = [i.replace(',','') for i in names1]
    return names1
    #raise NotImplementedError()
names()

# In[4]:

assert len(names()) == 4, "There are four names in the simple_string"

# In[ ]:


def grades():
    imiona = []
    oceny = []
    with open ( "notatki/Coursera_Algorytmy/Data_Science_In_Python/grades.txt", "r", 1 ) as file:
        grades = file.read().split('\n')
        for line in grades:
            try:
                imiona.append(line.split(':')[0])
                oceny.append(line.split(':')[1])
            except IndexError: pass
        #lines = file.readlines()
    #lines = file.readlines()
    return([j.strip() for i,j in zip(oceny,imiona) if i.strip()=='B'])

grades()
#print(len(grades())==16)
# In[ ]:


assert len(grades()) == 16

# In[ ]:


def logs1():
    hosts = []
    user_names = []
    times = []
    request = []


    with open( "notatki/Coursera_Algorytmy/Data_Science_In_Python/logdata.txt", "r", 1 ) as file1:
        logdata = file1.read().split( '\n' )
        for line in logdata:
            try:
                hosts.append( line.split( '-', 1 )[0].strip() )

                user_names.append( line.split( '-', )[1].strip() )
                times.append( line.split( ' ', 1 )[2].strip() )
                request.append( line.split( '-' )[3].strip() )
            except IndexError:
                pass
        # lines = file.readlines()
    # lines = file.readlines()
    return (user_names)

logs1()
#print(len(logs()))
# 979
# In[ ]:


def logs():
    hosts = []
    user_names = []
    times = []
    request = []
    full_list = []
    example_dict = {}


    with open( "notatki/Coursera_Algorytmy/Data_Science_In_Python/logdata.txt", "r", 1 ) as file1:
        logdata = file1.read().split( '\n' )
        for line in logdata:
            try:
                #print(line.split())
                splitting=line.split()
                #hosts.append(splitting[0])
                #user_names.append(splitting[2])
                #times.append(splitting[3]+' '+splitting[4])
                #request.append(splitting[5]+' '+splitting[6]+' '+splitting[7])
                full_list.append({"host": splitting[0], "user_name": splitting[2], "time": splitting[3].strip('[')+" "+splitting[4].strip(']'), "request": (splitting[5]+" "+splitting[6]+" "+splitting[7]).strip('\"')})
            except IndexError:
                pass
    return full_list
logs()
# In[ ]:


assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"

