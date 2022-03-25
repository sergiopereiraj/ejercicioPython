print("Hello World!")

nombre = "Yellow"

print(nombre)
variable_are_cool=2345*7323

print(variable_are_cool)

age = int(input('What is your age?\n'))+10
# CHANGE THE CODE BELOW TO ADD 10 TO AGE
print("Your age is: "+str(age))

# Set the values for my_var1 and my_var2 here

my_var1="Hello"
my_var2="World"


## Don't change below this line
the_new_string = my_var1+' '+my_var2
print(the_new_string)

a = '</title>'
b = '</html>'
c = '<head>'
d = '</body>'
e = '<html>'
f = '</head>'
g = '<title>'
h = '<body>'

# ⬆ DON'T CHANGE THE CODE ABOVE ⬆
# ↓ start coding below here ↓

html_document=e+c+g+a+f+h+d+b

print(html_document)

total = int(input('How much money do you have in your pocket\n'))

# YOUR CODE HERE
if total>100:
    print("Give me your money!")
elif total>50:
    print("Buy me some coffee you cheap!")
elif total<=50:
    print("You are a poor guy, go away!")