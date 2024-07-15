class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

  def get_average(self, grades):
    print(grades)
    grade_total = 0
    avg_counter = 0
    for grade in grades:
      print(grade)
      grade_total += grade
      avg_counter += 1
      print(grade_total)
    return grade_total / avg_counter

    

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def is_passing(score):
    return self.score > 65

pieter.add_grade(Grade(100))
print(pieter.get_average([65, 56, 85, 40]))

  