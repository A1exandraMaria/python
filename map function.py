L1 = [1,2,3]
squares = map (lambda x: x**2, L1)

stri = f"this would print only map object memory place: {squares}. \nOne needs to convert map object into list"
print(stri)
print("converted into list:" + str(list(squares)))

#we need to first convert into list

