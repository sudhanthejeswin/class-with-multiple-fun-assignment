class MultipleFunction:
    def Subfields():
        subfields = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for field in subfields:
            print(field)
             
    def OddEven():
        num = int(input("Enter a number: "))
        if (num % 2) == 1:
            print(str(num) + " is an Odd number")
        else:
            print(str(num) + " is an Even number")

    def Elegible():
        gender = input("Your Gender Male: ")
        age = int(input("Your Age: "))
    
        if gender == "Male":
            if age >= 21:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif gender == "Female":
            if age >= 18:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            print("Invalid Gender Input")

    def percentage(subject1, subject2, subject3, subject4, subject5):
        marks = [subject1, subject2, subject3, subject4, subject5]
        total = sum(marks)
        percentage = (total / (5 * 100)) * 100
        print(f"Subject1 = {subject1}")
        print(f"Subject2 = {subject2}")
        print(f"Subject3 = {subject3}")
        print(f"Subject4 = {subject4}")
        print(f"Subject5 = {subject5}")
        print(f"Total : {total}")
        print(f"Percentage : {percentage}")

    def triangle():
        height = float(input("Height: "))
        breadth = float(input("Breadth: "))
        area = (height * breadth) / 2
        print(f"Area formula: (Height * Breadth) / 2")
        print(f"Area of Triangle: {area}")
        
        height1 = float(input("Height1: "))
        height2 = float(input("Height2: "))
        breadth = float(input("Breadth: "))
        perimeter = height1 + height2 + breadth
        print(f"Perimeter formula: Height1 + Height2 + Breadth")
        print(f"Perimeter of Triangle: {perimeter}")
