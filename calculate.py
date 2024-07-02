def grade_calculation(line):
    line = line.strip() 

    elements = line.split(",") 

    name = elements[0]  
    note1 = int(elements[1]) 
    note2 = int(elements[2]) 
    note3 = int(elements[3])  


    result = note1 * (3/10) + note2 * (3/10) + note3 * (4/10)

    if result >= 90:
        grade = "AA"
    elif result >= 85:
        grade = "BA"
    elif result >= 80:
        grade = "BB"
    elif result >= 75:
        grade = "CB"
    elif result >= 70:
        grade = "CC"
    elif result >= 65:
        grade = "DC"
    elif result >= 60:
        grade = "DD"
    elif result >= 55:
        grade = "FD"
    else:
        grade = "FF"

    return f"{name} ------------------> {grade}\n"


with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(grade_calculation(line))
