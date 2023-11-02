# 10-30-23
# Convert from Quadratic to Graphing form
# Simple Github Repo
# kerbalist

# Prompt the user for a, b, and c
a = float(input("Enter the value 'a' : "))
b = float(input("Enter the value 'b' : "))
c = float(input("Enter the value 'c' : "))

#Calculate the h and k for graphing form
h = -b / (2 * a)
k = c - (b**2) / (4 * a)

# Display the graphing form
print(f"The graphing form of the quadratic equation is\n y = {a}(x - {h})^2 + {k}")
