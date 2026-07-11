class JustNotCoolError(Exception):
    pass



x = 2
try:
    # print(x / 0)
    raise JustNotCoolError("This isnt just cool man")
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed")
except NameError:
    print("NameError means something is probably undefined")
except ZeroDivisionError:
    print("An error occured while dividing")
except Exception as error:
    print(error)
else:
    print("No Errors!")
finally: 
    print("Im gonna print whether there's errror or not")