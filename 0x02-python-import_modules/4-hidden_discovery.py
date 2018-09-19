#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    mylist = dir(hidden_4)
    for x in mylist:
        if x[0:2] is "__":
            pass
        else:
            print(x)
