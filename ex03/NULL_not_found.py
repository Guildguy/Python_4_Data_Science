def NULL_not_found(object: any) -> int:
    if (object is None):
        print(f"Nothing: {object} {type(object)}")
    elif (type(object) == float):
        print(f"Cheese: {object} {type(object)}")
    elif (type(object) is bool):
        print(f"Fake: {object} {type(object)}")
    elif (object == 0):
        print(f"Zero: {object} {type(object)}")
    elif (object == ""):
        print(f"Empty: {type(object)}")
    else:
        print("Type not found")
        return (1)
    return (0)
