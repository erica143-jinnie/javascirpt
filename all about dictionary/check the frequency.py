test_dict = {'Codingal': 2,'is': 2, 'best' :2, 'For' : 2, 'Conding' :1}
print("The original Dictionary:"+str(test_dict))
K = 2
res = 0 
for key in test_dict:
    if test_dict[key]== K:
       res = res + 1
print("Frequency of K is:"+str(res))
       