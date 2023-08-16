def NULL_not_found(object: any)-> int:
    o = object.__class__

    if not object or object != object:
        if o is float:
            print("Cheese: nan", o)
        elif o is int and object == 0:
            print("Zero: 0 ", o)
        elif o is str and object == '':
            print("Empty: ", type(object))
        elif object == False:
            print("Fake: False", type(object))
        else:
            print("Nothing: None", o)
        return 0
    else:
        print("Type not Found")
        return 1
