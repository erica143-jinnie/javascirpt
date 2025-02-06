student_data = {'id1':
   {'name':['Shruti'],
   'class':['VIII'],
   'subjest_intergration': ['english,math,science']
},
'id2':
{'name':['David'],
   'class': ['VIII'],
   'subject_intergration':['english,math,science']
},
'id3':
    {'name':['Namirah'],
    'class':['VIII'],
    'subject_integration':['english,math,science']
},
'id4':
  {'name':['Arisha'],
  'class':['VIII'],
  'subject_integration':['english,math,science']
},
}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)