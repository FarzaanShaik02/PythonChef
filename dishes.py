user=input("Hi hello how are you doing ? \n")
user_input=input("Which reciepe are you looking for ??? \n")
r=user_input.title()
def Tomato():
        print("Follow the below steps for Tomato reciepe:\n")
        print("\n")
        print("1.First take tomatos according to your quantity and chop them into fine pieces.\n")
        print("2.And now take onions,green chilies,garlic(accorin to yur quantity*)and chop them evenly into pieces.\n")
        print("3.In next step on the stove,take a bowl and add oil\n")
        print("4.After oil is heated,add ur chopped onions,green chilies,garlic and set the flame on medium and let it cook for 5-10 minutes\n")
        print("5.Now after onions cooked well(it cahnges its colour*)add salt,turmeric to taste\n")
        print("6.mix them well and add chopped tomatoes to it and let it boil for 2 minutes\n")
        print("7.After the tomotoes boiled for 2 minutes add red chilly powder and after mixing it well add water to it and let it cook for 10 minutes more.\n")
        print("8.Ater 10 minutes of the stove and that's it your tomato curry is ready to be stuffed witha anything\n")
        print("\n")
        print("______Enjoy it______")
def Tea():
        print("Follow the below steps for Tea reciepe:\n")
        print("\n")
        print("1.First take milk according to your quantity and let it boil.\n")
        print("2.And now add tea powder,sugar to it let it boil for 5 minutes more.\n")
        print("3.That's it your tea is ready.\n")
        print("\n")
        print("______Enjoy it______")

'''not only these you can add many more here..I'm just going with 2 recipes that's it!'''
if r=="Tomato":
    Tomato()
elif r=='Tea':
    Tea()
else:
    pass
