def average(nums):
    sum = 0

    for i in range(0,len(nums)):
        sum += nums[i]

    return sum/len(nums)

def main():
    nums = [1, 3, 5, 7, 9]
    print("평균값은 {}입니다.".format(average(nums)))

if __name__ == "__main__":
    main()

