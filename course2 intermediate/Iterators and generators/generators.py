# Write your code below: 
def class_standing_generator():
  yield 'Freshman'
  yield 'Sophomore'
  yield 'Junior'
  yield 'Senior'

class_standings = class_standing_generator()

for classes in class_standings:
  print(classes)
  
  
  
"""NEXT AND STOP ITERATION"""
def student_standing_generator():
  student_standings = ['Freshman','Senior', 'Junior', 'Freshman']
  # Write your code below:

  for students in student_standings:
    if students == 'Freshman':
      yield 500
  
  standing_values = student_standing_generator()

  print(next(standing_values))
  print(next(standing_values))
  print(next(standing_values))



"""Generator Expresions"""
def cs_generator():
  for i in range(1,5):
    yield "Computer Science " + str(i)

# Write your code below:

cs_courses = cs_generator()
for courses in cs_courses:
  print(courses)

cs_generator_exp = ("Computer Science {}".format(i) for i in range(1,5))

for generator_exp in cs_generator_exp:
  print(generator_exp)
  
  
"""Generators Method Send Part 5"""

MAX_STUDENTS = 50

def get_student_ids():
  student_id = 1
  while student_id <= MAX_STUDENTS:
    # Write your code below
    n = yield student_id

    if n != None:
      student_id = n
      continue
    
    student_id += 1

student_id_generator = get_student_ids()
for i in student_id_generator:
  # Write your code below
  if i == 1:
    i = student_id_generator.send(25)
  print(i)
  
  
"""Part 6 Generator Methods: throw()
"""

def student_counter():
  for i in range(1,5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  # Write your code below:
  if student_id > 100:
        student_generator.throw(ValueError, "Invalid student ID")

  print(student_id)
  
  
"""PART 7 Generator Methods: close()
"""

def student_counter():
  for i in range(1,5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  print(student_id)
  # Write your code below:

  if student_id >= 100:
    student_id.close
    
    
    
"""Connecting Generators PART 8
"""

def science_students(x):
  for i in range(1,x+1):
    yield i

def non_science_students(x,y):
  for i in range(x,y+1):
    yield i
  
# Write your code below
def combined_students():
    yield from science_students(5)
    yield from non_science_students(10,15)
    yield from non_science_students(25,30)

student_generator = combined_students()

for students in student_generator:
  print(students)
  
  
  
"""Generator pipelines part 9"""


# def number_generator():
#   i = 0
#   while True:
#     yield i
#     i += 1
    
# def even_number_generator(numbers):
#   for n in numbers:
#     if n % 2 == 0:
#       yield n

# even_numbers = even_number_generator(number_generator())

# for e in even_numbers:
#   print(e)
#   if e == 100:
#     break


def course_generator():
    yield ("Computer Science", 5)
    # Write your code below:
    yield ("Art",10)
    yield ("Business", 15)

def add_five_students(courses):
  for course, num_students in courses:
    yield (course, num_students + 5)

increased_courses = add_five_students(course_generator())

for i in increased_courses:
  print(i)



"""review"""
def summa():
    yield 'Summa Cum Laude'

def magna():
    yield 'Magna Cum Laude' 

def cum_laude():
    yield 'Cum Laude'

def honors_generator(gpas):
  for gpa in gpas:
    if gpa > 3.9:
      yield from summa()
    elif gpa > 3.7:
      yield from magna()
    elif gpa > 3.5:
      yield from cum_laude()


def graduation_countdown(days):
  while days >= 0:
    days_left = yield days
    if days_left != None:
      days = days_left
    else:
      days -= 1


days = 25
countdown_generator = (day for day in range(days, -1,-1))
grad_days = graduation_countdown(days)
for day in grad_days:
  if day == 15:
    grad_days.send(10)
  elif day == 3:
    grad_days.close()
  print("Days Left: " + str(day))


days = 25
gpas = [3.2, 4.0, 3.6, 2.9]
honors = honors_generator(gpas)
for honor_label in honors:
  print(honor_label)