class Student:
    # Constructor
    def __init__(self, name, email, age):

        # Validate student details
        if name.strip() == "":
            raise ValueError("Student name cannot be empty.")
        if "@" not in email:
            raise ValueError("Email must contain @.")

        if age <= 0:
            raise ValueError("Age must be a positive number.")

        # Store student details
        self.__name = name.strip()
        self.__email = email.strip()
        self.__age = age

        #The double underscores show that it is a private attributes
        #This shows Encapsuation of data
        #I use Public getters to access them
        #This is so that they cannot be easily changed

        self.__enrolled_courses = []

    # Getters
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_age(self):
        return self.__age

    def get_enrolled_courses(self):
        return self.__enrolled_courses


    # Add a course to the student's list
    def add_course(self, course):
        if course not in self.__enrolled_courses:
            self.__enrolled_courses.append(course)

    # Enrol student in a course
    def enrol_in_course(self, course):
        course.enrol_student(self)

    # Display student's courses
    def view_courses(self):

        print("\nCourses enrolled in by " + self.__name + ":")

        if len(self.__enrolled_courses) == 0:
            print("No courses enrolled yet.")
        #We use a simple loop to display all the courses taken by a student
        else:
            for course in self.__enrolled_courses:
                print("- " + course.get_course_name())


class Course:
    # Constructor
    def __init__(self, course_name, duration, max_students):

        # Validate course details
        if course_name.strip() == "":
            raise ValueError("Course name cannot be empty.")

        if duration <= 0:
            raise ValueError("Course duration must be greater than zero.")

        if max_students <= 0:
            raise ValueError("Maximum students must be greater than zero.")

        # Store course details
        self.__course_name = course_name.strip()
        self.__duration = duration
        self.__max_students = max_students

        # Store enrolled students
        self.__enrolled_students = []

    # Getters
    def get_course_name(self):
        return self.__course_name

    def get_duration(self):
        return self.__duration

    def get_max_students(self):
        return self.__max_students

    def get_enrolled_students(self):
        return self.__enrolled_students


    # Enrol a student in the course
    def enrol_student(self, student):
        # Check if student is already enrolled
        if student in self.__enrolled_students:
            raise ValueError(student.get_name() + " is already enrolled in " + self.__course_name + ".")

        # Check course capacity
        if len(self.__enrolled_students) >= self.__max_students:
            raise ValueError(self.__course_name + " has reached its maximum capacity.")

        # Add student to course
        self.__enrolled_students.append(student)

        # Add course to student's list
        student.add_course(self)

        print(student.get_name() + " has successfully enrolled in " + self.__course_name + ".")


    # Display students enrolled in the course
    def view_students(self):

        print("\nStudents enrolled in " + self.__course_name + ":")

        if len(self.__enrolled_students) == 0:
            print("No students enrolled yet.")
        else:
            for student in self.__enrolled_students:
                print("- " + student.get_name())


print(" STUDENT AND COURSE MANAGEMENT ")


# Create student objects
student1 = Student("Oreoluwa Oladejo", "ore@example.com", 20)
student2 = Student("David Johnson", "david@example.com", 21)
student3 = Student("Esther Williams", "esther@example.com", 19)


# Create course objects
course1 = Course("Python Programming", 12, 2)
course2 = Course("Database Management", 8, 5)


print("\nStudent objects created successfully.")
print(student1.get_name())
print(student2.get_name())

print("\nCourse objects created successfully.")
print(course1.get_course_name())
print(course2.get_course_name())


#This shows the connection of the 2 classes
#It shows their relationship
#It doesnt haveto be inheritance or all that 
print("\n COURSE ENROLMENT ")

student1.enrol_in_course(course1)
student2.enrol_in_course(course1)
student1.enrol_in_course(course2)


#This views courses of the students
student1.view_courses()
student2.view_courses()

#This shows how many students in each course
course1.view_students()
course2.view_students()



print("\n TEST DUPLICATE ENROLMENT ")

try:
    student1.enrol_in_course(course1)

except ValueError as error:
    print("Error: You are already enrolled in this course")


print("\nTEST COURSE CAPACITY ")

try:
    student3.enrol_in_course(course1)

except ValueError as error:
    print("Error:This course is full to the max")


print("\nTEST STUDENT VALIDATION ")

try:
    invalid_student = Student("", "invalid@example.com", 20)

except ValueError as error:
    print("Error: " + str(error))
    #This calls that previous valuerror that shows the name cannot be empty

try:
    invalid_student = Student("John Doe", "johngmail.com", 20)

except ValueError as error:
    print("Error: " + str(error))
    #This calls the valueerror that shows that an email must have @

try:
    invalid_student = Student("John Doe", "john@example.com", -5)

except ValueError as error:
    print("Error: " + str(error))
    #This calls the value error that shows that says the age cannot be negative


print("\n TEST COURSE VALIDATION ")

try:
    invalid_course = Course("", 12, 10)

except ValueError as error:
    print("Error: " + str(error))


try:
    invalid_course = Course("Java Programming", 0, 10)

except ValueError as error:
    print("Error: " + str(error))


try:
    invalid_course = Course("Java Programming", 12, 0)

except ValueError as error:
    print("Error: " + str(error))

