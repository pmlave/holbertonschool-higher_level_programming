if __name__ == "__main__":
    from sys import argv
    x = 0
    for i in range(1, len(argv)):
        x += argv[i]
    print(x)
