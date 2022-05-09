#one.py

#defined this function
def func():
    print("Func() IN ONE.PY")

#print out this statement whenever you call one.py
print("Top level in one.py")

#if one.py is the main script, this will be printed out
if __name__ == "__main__":
    print("one.py is being run directly!")
#if it isn't set to main, the this will print out
else:
    print("one.py has been imported!")