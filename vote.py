# a program to vote using Paillier
import key_product
import encrypt
import decrypt


def maxcand(x):
    m = x[max(x, key=x.get)]
    s = ''
    for i in x.keys():
        if x[i] == m:
            s += str(i+1)+' '
    if len(s) > 2:
        print('第 %s名候选人并列选票数第一！highest vote选票数均为%i' % (s, m))
    else:
        print('第%i位候选人获得最高票数candidate who get the highest！number of vote选票数为%i' % (max(x, key=x.get) + 1, m))


x = 16
k = key_product.main(x)
pub, pri = k[0], k[1]

candidate = eval(input("请输入候选者人数please input the candidate number："))
voter = eval(input("请输入投票者人数please input the voter number："))
x = {}
for i in range(candidate):
    x[i] = 1


for i in range(voter):
    print("-" * 10 + "请第%i位投票者为候选者投票please the %i voter to vote for the candidate" % (i+1, i+1) + '-' * 10)
    for k in range(candidate):
        m = eval(input('请为第%i位候选者投票please vote for the %i candidate:' % (k+1, k+1)))
        x[k] *= encrypt.main(pub, m)
    print('对投票结果进行加密并发送给主办方send the results to the sponsor')

print('加密后统计结果：results')
for i in range(candidate):
    print('第%i位候选人获得选票的加密结果candidate：%i' % ((i+1), x[i]))
    x[i] = decrypt.main(pri, x[i], pub[0])
print('-'*10+'解密后结果after decryption'+'-'*10)
for i in range(candidate):
    print('第%i位候选人candidate get 获得%i选票vote' % ((i+1), x[i]))
print('---' * 10)
maxcand(x)
print('---'*10)
