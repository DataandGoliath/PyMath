from __future__ import division
import re
import sys
#Simple calculator script
#Get problem from user
math=raw_input(": ")
#Split up user input
#math=math.split()
def solve(problem):
  #Check for letters and prevent errors
  if re.search("[a-zA-Z]+", problem):
    print("Sorry, letters aren't allowed.")
    sys.exit()
  #Replace '^' with '**'
  problem=problem.replace("^","**")
  solved=eval("%s"%(problem))
  return solved
print(solve(math))
