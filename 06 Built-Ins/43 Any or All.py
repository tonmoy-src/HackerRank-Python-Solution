#Author: Tonmoy M
#URL: https://qinetique.github.io

N = int(input())
arr = input().split()
print(all(int(i) > 0 for i in arr) and any(i == i[::-1] for i in arr))