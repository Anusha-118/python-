class student:
    rollno=123
    name="anusha"
    branch="it"
    def read(self):
        name="muskan"
        print(name)
        print("instance variable=",s.branch)
        print("reading")

s=student()
print("rollno=",s.rollno)
print("name=",s.name)
print("branch=",s.branch)
s.read()
