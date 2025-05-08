students_names=
["sanjay","rahul","wasim","ramesh","ajay","sartaj","priya"]
students_marks=[35,50,20,45,25,40,25,25]

marks_perc =[]
for x in students_marks:
    res =(x/50)*100
    marks_perc.append

print(marks_perc)

# line chart
def marks_line_chart():
  plt.plot(students_names,students_marks)
  plt.title("students marks graph")
  plt.xlabel("students names")
  plt.ylabel("students marks")
  plt.show()

marks_line_chart()
#bar chart
def percentage_bar_chart():
  plt.bar(students_names,marks_perc)
  plt.title("students' percentage graph")
  plt.xlabel("student names")
  plt.yalabel("students names")
  plt.show()
percentage_bar_chart()