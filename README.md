# pail_vote
a homework , uses Paillier to help voting fairness

基于Paillier算法的匿名电子投票流程实现

![image](https://user-images.githubusercontent.com/103557716/202181746-b30ea710-3348-492b-a512-2191ce3da192.png)
**public key**(N,g) **private key**(lambda,u)

environment:***python***

**import:random,numpy,math**

## prime.py:Miller Rabin
```
input:n(int)
output:True or False
```

## key_product.py

```
import prime
input:n(int) # the bits of the prime
output:public key, private key
```

## encrypt.py
```
input:public key, plaintext(int)
output:cipher
```

## decrypt.py
```
input:private key, cipher(int), N(p*q)
output:decrypt_text(int)
```

## add.py
```
input1:222
input2:333
output:555(input1+input2)
```

## vote.py
well, all in the program.

目前存在问题：
* 当key_product.py中的input设置为16及其以下时，所有运行正常，超出16以上结果出现问题
* 有趣的是，如果将encrypt.py中的cr变量设置为1，不再是随机数的N次方，素数的位数可以扩充到26bits以下没有问题，怀疑是素数过大，素性检验出现问题。

problems：
* When the input in key_product.py is set to 16 or below, all operations are normal. If the input exceeds 16, problems occurs.
* Interestingly, if the cr variable in encrypt.py is set to 1, no longer the N power of a random number. The number of bits of a prime number can be expanded to less than 26 bits. It is suspected that the prime number is too large and the primality test goes wrong
