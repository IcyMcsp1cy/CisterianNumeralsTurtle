import turtle
myPen = turtle.Turtle()
myPaper = turtle.Screen()

# Ones place
def drawUnits(unit):
    if unit == 1:
        myPen.goto(0,100)
        myPen.goto(66,100)
        myPen.goto(0,100)
        myPen.goto(0,0)
    elif unit == 2:
        myPen.goto(0,50)
        myPen.goto(66,50)
        myPen.goto(0,50)
        myPen.goto(0,0)
    elif unit == 3:
        myPen.goto(0,100)
        myPen.goto(66,50)
        myPen.goto(0,100)
        myPen.goto(0,0)
    elif unit == 4:
        myPen.goto(0,50)
        myPen.goto(66,100)
        myPen.goto(0,50)
        myPen.goto(0,0)
    elif unit == 5:
        myPen.goto(0,50)
        myPen.goto(66,100)
        myPen.goto(0,100)
        myPen.goto(0,50)
        myPen.goto(0,0)
    elif unit == 6:
        myPen.goto(0,100)
        myPen.pencolor("white")
        myPen.goto(66,100)
        myPen.pencolor("black")
        myPen.goto(66,50)
        myPen.pencolor("white")
        myPen.goto(0,50)
        myPen.pencolor("black")
        myPen.goto(0,0)
    elif unit == 7:
        myPen.goto(0,100)
        myPen.goto(66,100)
        myPen.goto(66,50)
        myPen.goto(66,100)
        myPen.goto(0,100)
        myPen.goto(0,0)
    elif unit == 8:
        myPen.goto(0,50)
        myPen.goto(66,50)
        myPen.goto(66,100)
        myPen.goto(66,50)
        myPen.goto(0,50)
        myPen.goto(0,0)
    elif unit == 9:
        myPen.goto(0,100)
        myPen.goto(66,100)
        myPen.goto(66,50)
        myPen.goto(0,50)
        myPen.goto(0,0)
    else:
        pass

# Tens place
def drawTens(ten):
    if ten == 1:
        myPen.goto(0,100)
        myPen.goto(-66,100)
        myPen.goto(0,100)
        myPen.goto(0,0)
    elif ten == 2:
        myPen.goto(0,50)
        myPen.goto(-66,50)
        myPen.goto(0,50)
        myPen.goto(0,0)
    elif ten == 3:
        myPen.goto(0,100)
        myPen.goto(-66,50)
        myPen.goto(0,100)
        myPen.goto(0,0)
    elif ten == 4:
        myPen.goto(0,50)
        myPen.goto(-66,100)
        myPen.goto(0,50)
        myPen.goto(0,0)
    elif ten == 5:
        myPen.goto(0,50)
        myPen.goto(-66,100)
        myPen.goto(0,100)
        myPen.goto(0,50)
        myPen.goto(0,0)
    elif ten == 6:
        myPen.goto(0,100)
        myPen.pencolor("white")
        myPen.goto(-66,100)
        myPen.pencolor("black")
        myPen.goto(-66,50)
        myPen.pencolor("white")
        myPen.goto(0,50)
        myPen.pencolor("black")
        myPen.goto(0,0)
    elif ten == 7:
        myPen.goto(0,100)
        myPen.goto(-66,100)
        myPen.goto(-66,50)
        myPen.goto(-66,100)
        myPen.goto(0,100)
        myPen.goto(0,0)
    elif ten == 8:
        myPen.goto(0,50)
        myPen.goto(-66,50)
        myPen.goto(-66,100)
        myPen.goto(-66,50)
        myPen.goto(0,50)
        myPen.goto(0,0)
    elif ten == 9:
        myPen.goto(0,100)
        myPen.goto(-66,100)
        myPen.goto(-66,50)
        myPen.goto(0,50)
        myPen.goto(0,0)
    else:
        pass

# Hundreds place
def drawHundreds(hundred):
    if hundred == 1:
        myPen.goto(0,-100)
        myPen.goto(66,-100)
        myPen.goto(0,-100)
        myPen.goto(0,0)
    elif hundred == 2:
        myPen.goto(0,-50)
        myPen.goto(66,-50)
        myPen.goto(0,-50)
        myPen.goto(0,0)
    elif hundred == 3:
        myPen.goto(0,-100)
        myPen.goto(66,-50)
        myPen.goto(0,-100)
        myPen.goto(0,0)
    elif hundred == 4:
        myPen.goto(0,-50)
        myPen.goto(66,-100)
        myPen.goto(0,-50)
        myPen.goto(0,0)
    elif hundred == 5:
        myPen.goto(0,-50)
        myPen.goto(66,-100)
        myPen.goto(0,-100)
        myPen.goto(0,-50)
        myPen.goto(0,0)
    elif hundred == 6:
        myPen.goto(0,-100)
        myPen.pencolor("white")
        myPen.goto(66,-100)
        myPen.pencolor("black")
        myPen.goto(66,-50)
        myPen.pencolor("white")
        myPen.goto(0,-50)
        myPen.pencolor("black")
        myPen.goto(0,0)
    elif hundred == 7:
        myPen.goto(0,-100)
        myPen.goto(66,-100)
        myPen.goto(66,-50)
        myPen.goto(66,-100)
        myPen.goto(0,-100)
        myPen.goto(0,0)
    elif hundred == 8:
        myPen.goto(0,-50)
        myPen.goto(66,-50)
        myPen.goto(66,-100)
        myPen.goto(66,-50)
        myPen.goto(0,-50)
        myPen.goto(0,0)
    elif hundred == 9:
        myPen.goto(0,-100)
        myPen.goto(66,-100)
        myPen.goto(66,-50)
        myPen.goto(0,-50)
        myPen.goto(0,0)
    else:
        pass

# Thousands place
def drawThousands(thousand):
    if thousand == 1:
        myPen.goto(0,-100)
        myPen.goto(-66,-100)
        myPen.goto(0,-100)
        myPen.goto(0,0)
    elif thousand == 2:
        myPen.goto(0,-50)
        myPen.goto(-66,-50)
        myPen.goto(0,-50)
        myPen.goto(0,0)
    elif thousand == 3:
        myPen.goto(0,-100)
        myPen.goto(-66,-50)
        myPen.goto(0,-100)
        myPen.goto(0,0)
    elif thousand == 4:
        myPen.goto(0,-50)
        myPen.goto(-66,-100)
        myPen.goto(0,-50)
        myPen.goto(0,0)
    elif thousand == 5:
        myPen.goto(0,-50)
        myPen.goto(-66,-100)
        myPen.goto(0,-100)
        myPen.goto(0,-50)
        myPen.goto(0,0)
    elif thousand == 6:
        myPen.goto(0,-100)
        myPen.pencolor("white")
        myPen.goto(-66,-100)
        myPen.pencolor("black")
        myPen.goto(-66,-50)
        myPen.pencolor("white")
        myPen.goto(0,-50)
        myPen.pencolor("black")
        myPen.goto(0,0)
    elif thousand == 7:
        myPen.goto(0,-100)
        myPen.goto(-66,-100)
        myPen.goto(-66,-50)
        myPen.goto(-66,-100)
        myPen.goto(0,-100)
        myPen.goto(0,0)
    elif thousand == 8:
        myPen.goto(0,-50)
        myPen.goto(-66,-50)
        myPen.goto(-66,-100)
        myPen.goto(-66,-50)
        myPen.goto(0,-50)
        myPen.goto(0,0)
    elif thousand == 9:
        myPen.goto(0,-100)
        myPen.goto(-66,-100)
        myPen.goto(-66,-50)
        myPen.goto(0,-50)
        myPen.goto(0,0)
    else:
        pass

def main():
    myNumberInput = input("Enter an integer between 1 and 9999:")
    if myNumberInput.isnumeric():
        myNumber = int(myNumberInput)
        if myNumber > 1 and myNumber < 10000:
            unitsPlace = myNumber%10
            tensPlace = (myNumber%100)//10
            hundredsPlace = (myNumber%1000)//100
            thousandsPlace = myNumber//1000
            myPen.hideturtle()
            myPen.goto(0, -100)
            myPen.goto(0, 100)
            myPen.goto(0,0)
            drawUnits(unitsPlace)
            drawTens(tensPlace)
            drawHundreds(hundredsPlace)
            drawThousands(thousandsPlace)
        else:
            print("Integer not in range.")
            main()
    else:
        print("Input is not a integer.")
        main()

if __name__ == "__main__":
    main()


