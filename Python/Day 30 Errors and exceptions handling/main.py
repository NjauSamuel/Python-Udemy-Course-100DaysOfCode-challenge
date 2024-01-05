# In programming since things might not go as we plan out for them to go, we could handle this by catching exceptions.

# This is so because we want our program to fall gracefully and not catastrophically.

# while dealing with errors the four things that matter are:

# try: something that might cause an exception.

# except: Do this if there was an exception.

# else: Do this if there were no exceptions.

# finally: Do this no matter what happens.

# File not found error:
try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist. ")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed successfully. ")

# The final kind of error that can occur is one where the user themselves raises an error. an example is like. :

# ...
# finally:
#     raise TypeError("This is an error that I made up. ")

### When might you want to raise your own error.
## An example is in the following program.


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters. ")

bmi = weight / (height * height)
print(f"Your BMI is {bmi}")


# As the final project for this new found knowledge, we will update the Last pass password stuff that
# was built yesterday using JSON, and so we will have the knowledge required to do that.
