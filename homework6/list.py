def range_list(n):
    sum = []
    for i in range(1,1+n):
        sum += [i]
    return sum

def main ():
    n = 9
    print("list:", range_list(n))

if __name__ == "__main__":
    main()


