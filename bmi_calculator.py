import math

## BMI Calculator
# Calculates your BMI as well as tells you some things abouot your weight

name = input("What is your name?: ")

age = (int)(input("What is your age?: "))

weight = (int)(input("What is your weight in pounds?: "))

# Formula
# Formula: weight (lb) / [height (in)]2 x 703
# Calculate BMI by dividing weight in pounds (lbs) by height in inches (in) squared and multiplying by a
# conversion factor of 703

def convert_feet(feet):
    feet *= 12
    new_inches = feet
    return new_inches

feet_height = (int)(input("\nWhat is your height in feet?: "))
in_height = (int)(input("Inches?: "))

total_inches = in_height + convert_feet(feet_height)

bmi = (float)((weight/math.pow(total_inches, 2)) * 703)
bmi = round(bmi, 2)

print("\n\n\n                           ", name.title(), ", this means your BMI is", bmi)

if (bmi > 30.0):
    print(
    """
                I would suggest that you go see a doctor to discuss your health and possible options
                for weight loss. 
                
                This does not mean the end but having a BMI, this high is something to pay attention
                to as it can have some heavy health consequences
    
    
    """
    )
elif (bmi > 28.0 and bmi < 29.9):
    print(
    """
                You are doing good however you are getting close to being obese. I would consider that
                you look into forms of weight loss and correcting any problems that you feel you may be
                having. You got this!
    
    """
    )
    
elif(bmi > 25.0 and bmi < 28.0):
    print(
    """    
                Nice! You are right on the climb to being in a normal weight category! Keep working
                towards it! You will get there soon!
    
    """
    )
    
elif(bmi > 18.5 and bmi < 25):
    print(
    """   
                Great! You are in the normal weight category for your height! Good Job!
    
    """
    )
    
    
elif(bmi < 18.5):
    print(
    """   
                You are under the average bmi for people of your height and weight. I would consider
                looking at resources which could help you lose weight.
    
    """
    )


input("Press ENTER to exit the program.")