


# Asking user to enter the price they would like to pay.
# Asking the user to enter what the distance is. 

package_price = float(input("Please enter the amount you'd like to pay: "))
distance = float(input("please enter the total distance in KM's: "))

# Asking the users to answer 4 questions based on options that they would require.
# They simply have to answer with 1 or 0 as their parameters.
# Answers are then converted into integers.

shipping_question = int(input("Would like to send it via air which is 0.36 per KM or freight which is 0.25 per KM? Type 1 for air or 2 for freight: "))

insurance_question = int(input("Would you like full insurance which is 50 per KM or limited insurance which is 25 per KM? Type 1 for full or 2 for limited: "))

gift_question = int(input("Would you like a gift which is 15 or no gift? Type 1 for gift or 2 for no gift: "))

delivery_question = int(input("Would you like priority which is 100 or standard delivery at 20? Type 1 for priority or 2 for standard: "))


# Variables have been created for each option and their given price as the assigned value.
# air and freight costing is calculated by the distance multiplied by the going the rate.
# no_gift = 0 beacuse their is no cost associated with it.

air                 = 0.36 * distance
freight             = 0.25 * distance
full_insurance      = 100
limited_insurance   = 50
gift                = 15
no_gift             = 0
priority_delivery   = 100
standard_delivery   = 20

# There are four control statements, one for each question on the different costs.
# The total is all the users' options added together. This calculates the users total cost.
# The addition assignment operator is used ("+=") to add the users decision to the "total" variable.
# If the user did not select option "1" on any of the questions, it defaults to option "2". 
# It then adds that value of option 2 to the total cost.
# The answer is then rounded off to two decimal places.

total = 0

if shipping_question == 1:
    total += air
else:
    total += freight 

if insurance_question == 1:
    total += full_insurance
else:
    total += limited_insurance

if gift_question == 1:
    total += gift
  
if delivery_question == 1:
    total += priority_delivery
else:
    total += standard_delivery

print(round(total, 2))
