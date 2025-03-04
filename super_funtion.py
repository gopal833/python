class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")
class Student(Chef):
    def cook(self):
        super().make_chicken()
        print("student: added some salt and pepper")
student_instance = Student()
student_instance.cook()  # The chef makes a chicken