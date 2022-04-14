def str2list(text: str, default_value: float =-999):
    try:
        return float(text)
    except ValueError:
        return default_value


nums = []
num = 0

while num != '-1':
    num = input("x=?")
    nums.append(str2list(num, -999))

number1 = []
for i in range(len(nums)):
    if nums[i] > 0:
        number1.append(nums[i])

print("입력된 값은 {} 입니다.".format(number1))

