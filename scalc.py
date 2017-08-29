#Simple calculator script
#Get problem from user
math=raw_input(": ")
#Split up user input
#math=math.split()
def solve(problem):
  solved=exec("print(%s)"%(problem))
  return solved
  
print(solve(math))
