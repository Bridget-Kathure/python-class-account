
# class Student:
#            name = "Agnes"
#            school  = "Akirachix"
#            code = 79
#            age = 20


class Student:
      school = "Akirachix"
      def __init__(self,first_name, last_name, age, country,code):
                 self.first_name = first_name
                 self.last_name = last_name
                 self.age = age
                 self.country = country
                 self.code = code

      def greet_student(self):
              greeting = f"Hello {self.first_name}, welcome to {self.school}. Your code is {self.code}."
              return greeting
      def year_of_birth(self):
              return f"Hello{self.first_name}, you were born in {2024-self.age}."
      def full_name(self):
              return f"Hello, your names are {self.first_name}{self.last_name}"
      def initials(self):
              return f"Hello, {self.first_name},your initials are {self.first_name[0]}.{self.last_name[0]}"
      def check_minor(self):
              if self.age<18:
                      return f"you are a minor."
              else:
                      return f"You are an adult."
      def enroll_student(self):
              if 
              