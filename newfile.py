age = int(input("Enter your age: "))

if age >= 18:
    print("You can open")
else:
    print("You can't open")

# إصلاح استقبال الاسم كسلسلة نصية (string)
name = input("Enter your name, I guess your name is Nassim anyway enter the name: ")

# التحقق من الاسم بشكل صحيح
if name == "nassim":
    print("I told you no?")
else:
    print("I told you to enter your right name!")

# إعادة التحقق إذا كان الاسم "nassim"
if name == "nassim":
    print("You are always welcome!")