# calculate area of a circle

radius = int(input('enter radius in meters:'))
area = 3.142 * radius**2
print(area)


# if statement to print formatted response

if radius < 50:
	print(f'your {area}m circle is small')
elif radius <200:
	print(f'your {area}m circle is medium')
else:
	print(f'your {area}m circle is yuge')
	
	
