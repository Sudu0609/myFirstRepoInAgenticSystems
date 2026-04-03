def grade_students(studentt_list):
  result = {}
  
  for student in student_list:
    name = student['name']
    score =student['score']
    if score >=90:
      grade ='A'
    elif score >=75:
      grade ='B'
    elif score >=60:
      grade ='C'
    else:
      grade ='F'
      
    return result
    
  #Test data 
    students = [
      {'name': 'Alice', 'score': 92},
      {'name': 'Bob',   'score': 74},
      {'name': 'Carol', 'score': 61},
      {'name': 'Dave',  'score': 45}
  ]
  
  print(grade_students(students))
