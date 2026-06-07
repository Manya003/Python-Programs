# Parent Class
class Student:

    def __init__(self, name, rollno):
        self.name = name            # Public variable
        self._rollno = rollno       # Protected variable

    def show(self):
        print("Name:", self.name)
        print("Roll No:", self._rollno)


# Child Class
class MCAStudent(Student):

    def __init__(self, name, rollno, marks):

        super().__init__(name, rollno)
        self.__marks = marks        # Private variable

    # Setter
    def set_marks(self, marks):
        self.__marks = marks

    # Getter
    def get_marks(self):
        return self.__marks

    def display(self):
        self.show()
        print("Marks:", self.__marks)


# Object Creation
s = MCAStudent("Manya", 22, 90)

print("Using Getter:")
print("Marks =", s.get_marks())

print()

print("Using Setter:")
s.set_marks(95)
print("Updated Marks =", s.get_marks())

print()

print("Protected Variable Access:")
print(s._rollno)

print()

print("Display Function:")
s.display()