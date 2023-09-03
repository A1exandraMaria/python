list_of_tuples = [("Monica",20),
                  ("Rachel",26),
                  ("Susan",17),
                  ("Brian",15),
                  ("Tracy",37)]

age = lambda whatever:whatever[1] >=18 #age is a function that gets the second index and sets criteria for it

can_drink = filter (age, list_of_tuples)

print(list(can_drink))