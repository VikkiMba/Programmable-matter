name = input('Enter file name: ')
lst=list()
lst2=list()
with open(name) as f:
    for line in f:
        
        #print(line)
        blops=line.rstrip()
        blop=blops.split()
        #for val in blop:
        my_lst = [float(val) for val in blop]#list_comprehension
        for num in my_lst:
            if num <= 3.5:
                lst.append(num)
            if num >=4: lst2.append(num)

            #num = float(val)
            #print(num)
    #text = f.read()
#print(text)
#print(type(text))
#print(type(line))
#print(blop)
#print(type(blop))

#print(lst)
#print(lst2)
import itertools
import matplotlib.pyplot as plt
import seaborn as sns

#for (f, b) in zip(lst2 ,lst):
    #print (f, b)

#print(type(my_lst))
with open('neu_sam_4b.csv', 'w') as fh:
    for (f, b) in zip(lst, lst2):
        print(f,',',b, file=fh)
ext=lst
force=lst2
plt.plot(ext, force)
plt.xlabel('Extension')
plt.ylabel('Force')
plt.title('sample with 0.25wt%')
plt.tight_layout()
plt.show()



    #for digit in lst:
        #print(digit, file=fh)