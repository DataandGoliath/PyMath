from __future__ import division
#Simple calculator script
#Get problem from user
math=raw_input(": ")
#Split up user input
#math=math.split()
def solve(problem):
  #Replace '^' with '**'
  problem=problem.replace("^","**")
  solved=eval("%s"%(problem))
  return solved
print(solve(math))
