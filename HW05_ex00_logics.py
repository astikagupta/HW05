#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################
#even odd
def even_odd():
   
	print "Enter a numeral:"
	try:
		x = int(raw_input(">"))
	except:
		print "Wrong input."	
		even_odd()
	if x%2 == 0:
		print "Even number"
	else:
		print "Odd number"
    

#ten by ten grid
def ten_by_ten():

	count = 0
	for i in range(10):
		print "\n"
		for j in range(10):
			count = count + 1
			print count,		#count, prints all the items horizontally instead of vertically
        
	print "\n"
	
# average	
def find_average():

	x=0
	count=0
	while True:
		print "enter a number or enter done"
		y = raw_input()
		if y == 'done': 
			break
		try:
			y = eval(y)
            
		except:
			print "wrong input.try again"
				
		else:
			x=x+y
			count=count+1
	average = x/count
	return average
##############################################################################
def main():
	even_odd()
	ten_by_ten()
	x=find_average()
	print x 
	
if __name__ == '__main__':
    main()
