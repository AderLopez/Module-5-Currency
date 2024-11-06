#BMI Calculator function recevives two number to calculate the BMI and returns two messages:

def bmi_calculator(weight, height):
    #Calculates BMI based on weight ranges.

    #calculating BMI using the following formula: BMI=w/h^2
    BMI = round(float(weight) / (float(height/100)**2), 1)


    #Classification of the BMI
    if BMI < 18.5:
        #print("You are Underweight")
        message = "You are Underweight"
    elif BMI >= 18.5 and BMI < 25:
        #print("You have a Normal Weight")
        message = "You have a Normal Weight"
    elif BMI >= 25 and BMI < 30:
        #print("You are Overweight")
        message = "You are Overweight"
    elif BMI >= 30 and BMI < 34.9:
        #print("You have a Obese Class I")
        message = "You have a Obese Class I"
    elif BMI >= 35 and BMI < 39.9:
        #print("You have a Obese Class II")
        message = "You have a Obese Class II"
    elif BMI >= 40:
        #print("You have a Obese Class III")
        message = "You have a Obese Class III"

    #Writing the elements variable information on a file called Bmi_information. txt
    with open('Bmi_Information.txt', 'w', encoding='utf-8') as Bmi_text:
        Bmi_text.write(message + '\n')
        message_2 = f"Weight: {weight} \nHeight:{height}  \nYour BMI is: {BMI}"
        Bmi_text.write(str(message_2)+ '\n')

    #Returning the information to be called on HMTL 
    return BMI, message

