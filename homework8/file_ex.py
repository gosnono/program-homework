def text2list(text):
    return [int(x) for x in text.split()]


def average(nums):
    return sum(nums) / len(nums)


def main():
    input_text = "1 3 5 7 9"
    # f = open("numbers1.txt")
    # input_text = f.readline().strip()

    f = open("numbers.txt")
    lines = f.readlines()
    nums = [int(x.strip()) for x in lines]
    print(nums)

    nums = []
    for line in f:
        token = line.strip()
        nums.append(int(token))

    # print("AAA{}EEE".format(input_text))
    # nums = text2list(input_text)
    # print("평균은", average(nums))


if __name__ == "__main__":
    main()
