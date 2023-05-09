


#--------------------------------------------------------
#------ Practical Your Age Full Deatils------------
#--------------------------------------------------------

# Input Age

age = int(input("What is yout Age ? ").strip())

print(age) # 27
print(type(age)) # <class 'str'>

age = int(input("What is yout Age ? ").strip())
print(int(age)) # 27 
print(age) # 27
print(type(age)) # <class 'int'>

# Get Age in All Time Units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("You lived for :")
print(f"{months} Months.") # 324 Months.
print(f"{weeks} Weeks.") # 1296 Weeks.
print(f"{days} Days.") # 9855 Days.
print(f"{hours:,} hours.") # 236,520 hours.
print(f"{minutes:,} minutes.") # 14,191,200 minutes.
print(f"{seconds:,} seconds.") # 851,472,000 seconds.


