def myAge(currentYear,myBrith):
    myAge = currentYear - myBrith
    return myAge
output = myAge(2024,2004)
print("My brith year:", output)


    
def areaOfRectangle(width, length):
    areaOfRectangle = width * length
    return areaOfRectangle
result = areaOfRectangle(4.0,3.0)
print("Area of rectangle:", result)



def area(pi,radius):
    areaOfCircle = pi * radius**2
    return areaOfCircle
result = area(3.14159,5)
print("Area of circle:", result)



def surfaceArea(l,b,h):
    a = l = b = h 
    surface = 6*(a*a)
    return surface
output = surfaceArea(5,5,5)
print("Surface Area of Cube is:", output)



def inCelsius(Fahrenheit):
    Celsius = (Fahrenheit - 32) * 5/9
    return Celsius
finalOutput = inCelsius(100)
print("Celsius:", finalOutput)



def givenNumber():
    number = int(input())
    intoMin = number // 60
    print(intoMin ,"min", number, "sec")
givenNumber()

    
def marksPercentage(marks,totalMarks):
    percentage = marks/totalMarks * 100
    return percentage
result = marksPercentage(int(input()),100)
print(result,"%")    


def BMIFormula(weight,height):
    BMI = weight / height**2
    return BMI
output = BMIFormula(15,25)
print("BMI:", output)


def volumeCal(height,radius,pi):
    volume = pi * (radius ** 2) * height 
    return volume
output = volumeCal(7, 1.5, 3.14159)
print("Volume of Cylinder:", output)