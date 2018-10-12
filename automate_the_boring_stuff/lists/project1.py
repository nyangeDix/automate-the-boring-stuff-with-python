def get_cats():
    catNames = []
    while True:
        print("Enter the name of cat" + str(len(catNames)))
        name = input()

        if name == '':
            break
            exit()
        catNames = catNames + [name]

        for name in catNames:
            print(' ' + name)

get_cats()
