inp = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

ints = [str(i) for i in list(range(10))]
res = 0

for line in inp.split('\n'):
    nums = [char for char in line if char in ints]
    res += int(nums[0] + nums[-1])

print(res)