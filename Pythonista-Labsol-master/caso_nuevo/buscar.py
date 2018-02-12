def readFile(srchItem):
    with open("alumnos.txt", "r") as file:
        file_content = file.readlines()
        file.close()

    templist = file_content

    for item in templist:
        if srchItem in item:
            print("Got it")
            print(item)








