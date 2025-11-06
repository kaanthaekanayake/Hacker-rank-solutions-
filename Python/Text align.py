"""
ljust: Aligns the string to the left, padding with spaces on the right.
  H----  syntax: steing.ljust(width, fillchar=' ') 
  fillchar is optional, default is space. and it used to fill the empty space.
rjust: Aligns the string to the right, padding with spaces on the left.
  ----H syntax: steing.rjust(width, fillchar=' ')
center: Centers the string, padding with spaces on both sides.
  --H-- syntax: steing.center(width, fillchar=' ')
"""
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


"""
 Before using these methods, get a paper and try to draw the output of each section by hand.
 This will help you understand how each method works and how to use them effectively in your code.
 and also u can how much space is needed on each side to achieve the desired alignment.
"""