
def hello(name):
    print(f"Hello {name}")
    
def year_of_birth(name,age):
    year = 2024 - age
    print(f"Hello {name}, you were born in {year}")

    def my_country(country = "Uganda"):
     print(f"Hello Akirachix from {country}")

   
# this function will only accept one arguments when calling it.
     def hello (name):
        print(f"hello{name}")

# To have a function accepts any number of arguments use one asteric
# use plural when passing your parameters
        def greet (*names):
           for name in names:
              print(f"Hello{name}")

    def add(x,y):
        sum = x + y
        return sum
     
    def create_sentence(**words):

        sentence = ""
        for word in words.values():
          sentence += word
          sentence += " "
        return sentence
#    using both positional and keyword arguments 
    def sum_and_greet(*args,**kwargs):
        """get sum"""
        total = 0
        for x in args:
            total+=x
            f = kwargs["first_name"]
            l = kwargs["last_name"]
            greeting = f"hello{f}{l},the total of your numbers is {total}"
        return greeting
         