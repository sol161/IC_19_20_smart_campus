# SMART CAMPUS INFORMATION SYSTEM

import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = []

# 1. STUDENT REGISTRATION
def registration():

    print("\n--- Student Registration ---")

    sid = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")

    math = int(input("Enter Math Marks: "))
    science = int(input("Enter Science Marks: "))
    english = int(input("Enter English Marks: "))

    average = (math + science + english) / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    cgpa = round(average / 10, 2)

    student = {
        "ID": sid,
        "Name": name,
        "Math": math,
        "Science": science,
        "English": english,
        "CGPA": cgpa,
        "Grade": grade
    }

    students.append(student)

    print("\nStudent Registered Successfully")

# 2. COURSE ENROLLMENT
def enrollment():

    print("\n--- Course Enrollment ---")

    sid = int(input("Enter Student ID: "))

    found = False

    for s in students:

        if s["ID"] == sid:

            found = True
            courses = []

            while True:

                course = input("Enter Course(done to stop): ")

                if course.lower() == "done":
                    break

                courses.append(course)

            s["Courses"] = courses

            print("Courses Enrolled Successfully")
            break

    if not found:
        print("Student Not Found")

# 3. MANAGE RECORDS
def records():

    print("\n--- Student Records ---")

    if len(students) == 0:
        print("No Records Available")
        return

    for s in students:
        print(s)

# 4. SORT & SEARCH IDS
def sortsearch():

    print("\n--- Sort & Search IDs ---")

    if len(students) == 0:
        print("No Records Available")
        return

    ids = []

    for s in students:
        ids.append(s["ID"])

    ids.sort()

    print("Sorted IDs:", ids)

    target = int(input("Enter ID to Search: "))

    if target in ids:
        print("ID Found")
    else:
        print("ID Not Found")

# 5. FEE CALCULATION
def fee():

    print("\n--- Fee Calculation ---")

    tuition = float(input("Enter Tuition Fee: "))
    hostel = float(input("Enter Hostel Fee: "))
    transport = float(input("Enter Transport Fee: "))

    total = tuition + hostel + transport

    print("Total Fee =", total)

# 6. FILE HANDLING
def filehandling():

    print("\n--- File Handling ---")

    if len(students) == 0:
        print("No Student Records Available")
        return

    with open("student_records.txt", "w") as file:

        file.write("ID,Name,CGPA,Grade\n")

        for s in students:

            file.write(
                f"{s['ID']},{s['Name']},{s['CGPA']},{s['Grade']}\n"
            )

    print("Records Saved Successfully")

    print("\n--- File Contents ---")

    with open("student_records.txt", "r") as file:
        print(file.read())

# 7. DIRECTORY SCANNING
def directory():

    print("\n--- Directory Scanning ---")

    files = os.listdir()

    for f in files:
        print(f)

# 8. PERFORMANCE ANALYSIS
def performance():

    print("\n--- Performance Analysis ---")

    if len(students) == 0:
        print("No Student Data Available")
        return

    df = pd.DataFrame(students)

    print("\nStudent Data\n")
    print(df)

    scores = df[["Math","Science","English"]].to_numpy()

    print("\nMean Scores:")
    print(np.mean(scores, axis=0))

    print("\nStatistical Summary:")
    print(df[["Math","Science","English"]].describe())

    plt.figure(figsize=(6,4))
    plt.bar(df["Name"], df["CGPA"])
    plt.title("CGPA Distribution")
    plt.xlabel("Students")
    plt.ylabel("CGPA")
    plt.show()

# MAIN MENU
while True:

    print("\n--- Smart Campus Information System ---")
    print("1.Student Registration")
    print("2.Course Enrollment")
    print("3.Manage Records")
    print("4.Sort & Search IDs")
    print("5.Fee Calculation")
    print("6.File Handling")
    print("7.Directory Scanning")
    print("8.Performance Analysis")
    print("9.Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        registration()

    elif choice == "2":
        enrollment()

    elif choice == "3":
        records()

    elif choice == "4":
        sortsearch()

    elif choice == "5":
        fee()

    elif choice == "6":
        filehandling()

    elif choice == "7":
        directory()

    elif choice == "8":
        performance()

    elif choice == "9":
        print("\nExiting System...")
        break

    else:
        print("Invalid Choice")