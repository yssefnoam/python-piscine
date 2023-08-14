def NULL_not_found(object: any)-> int:
    # print(object)
    # print(type(object))
    o = object.__class__
    print("object: ", type(object))

    if o is None:
        print("Nothing: None", type(object))
        return 0
    elif o is float and object == float("NaN"):
        print("Cheese: nan", type(object))
        return 0
    elif object is None:
        print("Nothing: None", type(object))
        return 0
    elif object is None:
        print("Nothing: None", type(object))
        return 0
    elif object is None:
        print("Nothing: None", type(object))
        return 0
    else:
        print("Type not Found")
        return 1
