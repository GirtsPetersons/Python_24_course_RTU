COLD_TEMP = 35
FEVER_TEMP = 37

temp = float (input("Kāda ir Jūsu temperatūra? "))

if temp <= COLD_TEMP:
    print("Vai jūtaties labi?")
elif temp > FEVER_TEMP:
    print("Iespējams drudzis")
else:
    print("Viss kārtībā")
              