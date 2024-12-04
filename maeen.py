try:
    namber_1 = int(input("enter the number 1 NOW OR U DIE"))
    namber_2 = int(input("enter the number 2 NOW OR U DIE"))

    result = namber_1 / namber_2

    print(result)
except ZeroDivisionError:
    print ("if you do the diviad by 0, YOU DIE")

except ValueError:
    print("enter number val or U DIE")

except NameError as ex:
    print("exeption is", ex)

except:
    print("YOU DIED OUT OF UNKNOWN CIRCUMSTANCES")

finally:
    print("this exists no matter what")