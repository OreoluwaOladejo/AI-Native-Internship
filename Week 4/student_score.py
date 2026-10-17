# Dictionary of students and their score lists
students = {}

# Keep displaying the menu until the user exits
while True:
    print("\n STUDENT SCORES ")
    print("1. Add student")
    print("2. Update student scores")
    print("3. Remove student")
    print("4. View student scores")
    print("5. Calculate totals and averages")
    print("6. Sort students by average score")
    print("7. Show passing scores")
    print("8. Exit")

    choice = input("Choose an option: ")

    # Adding students
    if choice == "1":
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty.")
        elif name in students:
            print("Student already exists.")
        else:
            scores = []
            number_of_scores = int(input("How many scores? "))

            for i in range(number_of_scores):
                score = float(input(f"Enter score {i + 1}: "))
                scores.append(score)

            students[name] = scores
            print("Student added successfully.")

    # UPdating scores
    elif choice == "2":
        name = input("Enter student name: ").strip()

        if name not in students:
            print("Student not found.")

        else:
            print("Current scores:", students[name])
            print("1. Add a score")
            print("2. Change a score")
            print("3. Remove a score")
            print("4. Replace all scores")

            action = input("Choose an option: ")

            if action == "1":
                new_score = float(input("Enter new score: "))
                students[name].append(new_score)
                print("Score added.")

            elif action == "2":
                print("Scores:", students[name])
                index = int(input("Enter score position to change (starting at 1): "))

                if 1 <= index <= len(students[name]):
                    new_score = float(input("Enter new score: "))
                    students[name][index - 1] = new_score
                    print("Score updated.")
                else:
                    print("Invalid score position.")

            elif action == "3":
                print("Scores:", students[name])
                index = int(input("Enter score position to remove (starting at 1): "))

                if 1 <= index <= len(students[name]):
                    students[name].pop(index - 1)
                    print("Score removed.")
                else:
                    print("Invalid score position.")

            elif action == "4":
                new_scores = []
                number_of_scores = int(input("How many scores? "))

                for i in range(number_of_scores):
                    score = float(input(f"Enter score {i + 1}: "))
                    new_scores.append(score)

                students[name] = new_scores
                print("Scores replaced.")

            else:
                print("Invalid option.")

    # Removing student
    elif choice == "3":
        name = input("Enter student name to remove: ").strip()

        if name in students:
            del students[name]
            print("Student removed.")

        else:
            print("Student not found.")

    # View scores
    elif choice == "4":
        name = input("Enter student name: ").strip()

        if name in students:
            print(f"Scores for {name}: {students[name]}")

        else:
            print("Student not found.")

    # Calclate totals and average
    elif choice == "5":
        if not students:
            print("No student records available.")

        else:
            for name, scores in students.items():
                total = sum(scores)

                # Avoid division by zero
                if scores:
                    average = total / len(scores)
                    print(f"{name}: Total = {total}, Average = {average:.2f}")
                else:
                    print(f"{name}: No scores recorded.")

    # Sort students by scores
    elif choice == "6":
        # Ignore students who have no scores
        students_with_scores = [
            (name, sum(scores) / len(scores))
            for name, scores in students.items()
            if scores
        ]

        # Sort by average, highest first
        students_with_scores.sort(key=lambda student: student[1], reverse=True)

        if students_with_scores:
            for position, (name, average) in enumerate(students_with_scores, start=1):
                print(f"{position}. {name}: {average:.2f}")
        else:
            print("No students with scores to sort.")

    # Passing scores
    elif choice == "7":
        passing_mark = float(input("Enter the passing mark: "))

        for name, scores in students.items():
            passing_scores = [
                score for score in scores
                if score >= passing_mark
            ]

            print(f"{name}: Passing scores = {passing_scores}")

    # Exiting the loop or menu
    elif choice == "8":
        print("Bye for now ")
        break

    else:
        print("Invalid choice. Try again.")