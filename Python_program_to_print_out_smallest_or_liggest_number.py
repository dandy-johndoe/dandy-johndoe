smallest = None
largest = -1
while True :
    inp = input("Enter a number: ")
    if inp == "done":
        break

    try :
        nig = int(inp)
    except:
        print("Invalid output")

    if smallest is None:
        smallest = nig

    elif nig < smallest:
        smallest = nig

    elif nig > largest:
        largest = nig

print("Maximum is", largest)
print("Minimum is", smallest)
