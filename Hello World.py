#Ask User for their name
name = input ("Whats Your Name ?").strip().title()
#Split User's name into first and last name
first, last = name.split()
#Say hello To User
print (f"Hello, {first}")
