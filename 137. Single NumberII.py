"""
    Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
    
    Note:
    
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
    
    Example 1:
    
    Input: [2,2,3,2]
    Output: 3
    Example 2:
    
    Input: [0,1,0,1,0,1,99]
    Output: 99
    
    
    
    数组为[2,2,2,3]，一共有四个元素，进行四次循环。
    
    第一次循环，b=(0000^0010)&1111=0010=2，a=(0000^0010)&1101=0000=0
    
    第二次循环，b=(0010^0010)&1111=0000=0，a=(0000^0010)&1111=0010=2
    
    第三次循环，b=(0000^0010)&1101=0000=0，a=(0010^0010)&1111=0000=0
    
    第四次循环，b=(0000^0011)&1111=0011=3，a=(0000^0011)&1100=0000=0
    
某个值nums[i]第一次出现的时候，b把它记录了下来，这时候a=0；接着第二次出现的时候，b被清空了，记录到了a里面；接着第三次出现的时候，b和a都被清空了。
如果一个数组中，所有的元素除了一个特殊的只出现一次，其他都出现了三次，那么根据我们刚刚观察到的结论，最后这个特殊元素必定会被记录在b中。
那么这次我们同样利用异或运算，看能不能设计出一种变换的方法让a和b按照上述变换规则，进行转换。
b=0时碰到x，就变成x；b=x时再碰到x，就变成0，这个不就是异或吗？所以我们也许可以设计b=b xor x。
但是当b=0时再再碰到x，这时候b还是要为0，但这时候不同的是a=x，而前两种情况都是a=0。所以我们可以设计成：b=(b xor x)&~a
同样道理，我们可以设计出：a=(a xor x)&~b

"""
def singleNumber(nums):
    a,b = 0, 0
    for num in nums:
        b = (b ^ num) & ~a  # when the third nums[i] coming, b need to be 1 again, but at this time previous nums[i] in a, so & ~a can set b to 1.
        a = (a ^ num) & ~b
    return b
