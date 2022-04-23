def text2list(nums):
    return nums


def count(nums):
    return len(nums)


def num_max(nums):
    n_sorted=sorted(nums)
    return n_sorted[-1]


def num_min(nums):
    n_sorted=sorted(nums)
    return n_sorted[0]


def average(nums):
    sum = 0
    
    for i in range(0,len(nums)):
        sum += nums[i]
    return sum/len(nums)


def main():
    f = open("numbers2.txt")
    lines = f.readlines()
    nums = [int(x.strip()) for x in lines]
    
    print(text2list(nums))
    print("총 갯수? ", count(nums))
    print("평균? ", average(nums))
    print("최댓값? ", num_max(nums))
    print("최솟값? ", num_min(nums))

if __name__ == "__main__":
    main()