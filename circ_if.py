# calculate area of a circle

radius = int(input('enter radius in meters:'))
area = 3.142 * radius**2
print(area)


# if statement to print formatted response

if area < 500:
	print(f'your {area:.3f}m circle is small')
elif area <2000:
	print(f'your {area:.3f}m circle is medium')
else:
	print(f'your {area:.3f}m circle is yuge')
	
	
