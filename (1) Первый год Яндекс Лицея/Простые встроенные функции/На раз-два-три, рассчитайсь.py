ans1 = int(input())
ans2 = int(input())
ans3 = int(input())
if ans1 < ans2:
    ans1, ans2 = ans2, ans1
if ans2 < ans3:
    ans2, ans3, = ans3, ans2
if ans1 < ans2:
    ans1, ans2 = ans2, ans1
print(ans1)
print(ans2)
print(ans3)