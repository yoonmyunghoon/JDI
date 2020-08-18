import sys
sys.stdin = open("4606_The Seven Percent Solution.txt")

while 1:
    URLs = input()
    if URLs == '#':
        break
    else:
        URLs1 = URLs.replace('%', '%25')
        URLs2 = URLs1.replace(' ', '%20')
        URLs3 = URLs2.replace('!', '%21')
        URLs4 = URLs3.replace('$', '%24')
        URLs5 = URLs4.replace('(', '%28')
        URLs6 = URLs5.replace(')', '%29')
        URLs7 = URLs6.replace('*', '%2a')
        print(URLs7)
