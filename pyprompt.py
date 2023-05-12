import os
command = ""

while command != "exit":
    command = str(input("Command Prompt: "))
    os.system(str(command))
print("Exited command prompt.")
