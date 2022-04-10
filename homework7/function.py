def text2list(text):
    list = text.split()
    nums = []
    for list in list:
        nums.append(int(list))
    return nums

def average(nums):
    return sum(nums)/len(nums)

def median(nums):
    half = len(nums)//2
    nums.sort()
    return nums[half]

def main():
    input_text = "5 10 3 4 7 "
    nums = text2list(input_text)
    print("주어진 리스트는", nums)
    print("평균값은 {:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))


if __name__ == "__main__":
    main()

