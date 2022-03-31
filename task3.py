import turtle # imports turtle graphics
def square(x,colors,times):  #draw squares with length x and  color
  t=turtle.Turtle()#constructer method that returns an instance of class turle
  t.pendown()#start making lines on the screen
  for j,color in enumerate(colors):#basically a loop, in this case there are 2 choices to loop through the counter and the value
    t.pencolor(colors[j])#colours iterate through our set colours
    x=x+10#increase size
    for i in range(times):#iterate as many times as user has specified
      t.forward(x)#forward
      t.right(90)#90 degree turn right 
  turtle.done()#done turtle pen up no more drawing.
#draw rectangles and color where x is the length and y = x+y is breadth
def rectangle(x,colors,times,y): #draws rectangle with legth x and color
  t=turtle.Turtle(); 
  t.pendown()
  for j,color in enumerate(colors): # gives us 2 chices to loop and value
    t.pencolor(colors[j])
    y=y + 10  # colours iterate 
    x=x+10   # this increases the size
    for i in range(times): #iterate the amount as time specified by the user
      t.forward(x) # forward 
      t.right(90)
      t.forward(y) # forward
      t.right(90) # right turn 90 degrees
      
     
  turtle.done() # completed turtle pen up no more drawing
# draw circles with radius x
def circle(x,colors):
  t=turtle.Turtle()
  for j,color in enumerate(colors):#counter basically a loop
    t.pencolor(colors[j])
    x=x+10
    t.pendown()
    t.circle(x)
  turtle.done()

#Error handling 

while True:
  choices=['circle','square','rectangle']
  choice=input('Please enter an option between square or circle:')
  if choice.lower() in choices:
    break
  else:
    print("Your choice wasnt in the original list of circle,square and rectangle please try again!")
    continue

colors=['red','orange','blue','green','yellow','violet']
if choice=='square':
  x= int(input("Please enter the length of the shape: "))
  times=int(input('how many times:'))
  square(x,colors,times)

if choice=='rectangle':
  x= int(input("Please enter the length of the shape: "))
  y= int(input("Please breadth: "))
  times=int(input('how many times:'))
  square(x,colors,times,y)

if choice=='circle':
  x= int(input("Please enter the radius shape: "))
  square(x,colors)