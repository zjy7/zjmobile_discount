import sys
import pyautogui
from base64 import b64decode
from io import BytesIO
from PIL import Image
import camelcase

def mainclolor():
    print('go')
    count = 0
    c = camelcase.CamelCase()
    txt = "hello world"
    print(c.hump(txt))

    x = 10
    y = 6.3
    z = 2j
    print(type(x))
    print(type(y))
    print(type(z))

    x = "awesome"
    print("Python is " + x)

    arr = [1, 2, 3, 4, 5]
    print(type(arr))

    for i in arr:
        print(i)

    print(len(arr))

    cars = ["Porsche", "Volvo", "BMW"]

    print(cars)

    thistuple = ("apple", "banana", "cherry")
    print(thistuple)

    thisset = {"apple", "banana", "cherry"}
    print(thisset)

    thisdict =	{
      "brand": "Porsche",
      "model": "911",
      "year": 1963
    }
    print(thisdict)

    for x in range(10):
        print(x)

    print(type(range(4)))

    mytuple = ("apple", "banana", "cherry")
    myit = iter(mytuple)
    print(type(myit))
    print(next(myit))
    print(next(myit))
    print(next(myit))
    # print(next(myit))

mainclolor()