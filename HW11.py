#Name: Connor Altland
#Class: 6th Hour
#Assignment: HW11

#1. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg


#import random library
import random
#Create a temperature variable, give it a value (random from 1 to 30).
n = random.randint(1,30)
#Make an if statement to see if temperature variable is above 20
#   - If yes, print it's hot
#   - If no, bring it to next if statement
if n > 20:
    print("Its to hot")
#Make an if statement to see if temperature variable is above 10
#   - If yes, print it's mild
#   - If no, print it's cold
if n > 10:
    print("Its mild")
else:
    print("Its to cold")
#Print "Thank you!" and end the code
print("Thank you!")