# Week 7 - Student and Course Domain Model

## Project Description

This project is a simple Student and Course Management Domain Model developed using Python and Object-Oriented Programming (OOP).

It represents students and courses, their information, and how students enrol in courses.

The program also uses validation to prevent invalid student information and course enrolments.

## Classes

### 1. Student

The Student class represents an individual student.

**Attributes:**
- name
- email
- age
- enrolled_courses

**Methods:**
- get_name()
- get_email()
- get_age()
- get_enrolled_courses()
- add_course()
- enrol_in_course()
- view_courses()

### 2. Course

The Course class represents a course available for student enrolment.

**Attributes:**
- course_name
- duration
- max_students
- enrolled_students

**Methods:**
- get_course_name()
- get_duration()
- get_max_students()
- get_enrolled_students()
- enrol_student()
- view_students()

## Relationship Between the Classes

The Student and Course classes have a many-to-many relationship.

A student can enrol in multiple courses, while a course can have multiple students.

The program maintains this relationship using lists.

## Validation Rules

The program applies the following validation rules:

**Student:**
- Name must not be empty.
- Email must contain @.
- Age must be a positive number.

**Course:**
- Course name must not be empty.
- Duration must be greater than zero.
- Maximum number of students must be a positive whole number.

**Enrolment:**
- A course cannot exceed its maximum capacity.
- A student cannot enrol in the same course twice.

Invalid values raise ValueError exceptions with appropriate error messages.

## OOP Concepts Used

- Classes and Objects
- Constructors
- Attributes and Methods
- Encapsulation

## Demo
Demo recording: [Add your demo link here]
