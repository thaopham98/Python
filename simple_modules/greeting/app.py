import greetings

print(greetings.hello("Thao")) # run with cli: python app.py

# # Import specific function
# from greetings import hello
# hello("Bob")  # Works directly, no "greetings." prefix

# # Import everything
# from greetings import *
# hello("Charlie")  # All functions available

# # Import with alias
# import greetings as g
# g.hello("Diana")