name = input("What is your name ? ")
ages = input(f"How old are You {name}? ")
ages = int(ages)
end = 100 - ages
print(f"Wow {name} in {end} years you will be 💯 years old!")
import datetime
currentYear = datetime.datetime.now().year
endYear = currentYear + end
print(f"It will be in {endYear}!")