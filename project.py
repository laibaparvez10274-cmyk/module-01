def result_card(name, marks):
    print("---- Result Card ----")
    print("Name:", name)

    total = 0
    for m in marks:
        total = total + m

    average = total / 3
    print("Total:", total)
    print("Average:", average)

    if average >= 80:
        print("Grade: A - Excellent Laiba!")
    elif average >= 60:
        print("Grade: B - Good!")
    else:
        print("Grade: C - Thora aur mehnat karo")

student = {
    "name": "Laiba",
    "marks": [85, 90, 78]
}

result_card(student["name"], student["marks"])