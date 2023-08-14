def all_thing_is_obj(object: any) -> int:
    o = object.__class__
    if o == list:
        print("List :", o)
    elif o is tuple:
        print("Tuple :", o)
    elif o is set:
        print("Set :", o)
    elif o is dict:
        print("Dict :", o)
    elif o is str:
        print("Brian is in the kitchen :", o)
    else:
        print('Type not found')
    return 42