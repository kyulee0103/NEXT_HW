num = int(input("enter any number: "))


def odd_set():
    for i in range(4):
        for j in range(9):
            print(f"{i*2+3} * {j+1} = {(i*2+3)*(j+1)}")
        print("****************************")


def even_set():
    for i in range(4):
        for j in range(9):
            print(f"{i*2+2} * {j+1} = {(i*2+2)*(j+1)}")
        print("****************************")


if num %2 == 0:
    even_set()

else:
    odd_set()