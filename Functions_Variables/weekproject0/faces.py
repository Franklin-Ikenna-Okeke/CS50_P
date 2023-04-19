def main():
    convert = input("Enter an input ")
    print(faces(convert))



def faces(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")


main()
