#正则规则
#规则中的字符刚好匹配到字符串中的功能

#字符组 []
   #[abc] 一个中括号只表示一个字符串的位置
   #[0-9] 根据ascii码匹配的

#[0-9] \d
#[A-Za-z0-9] \w
#空白（空格/tab/enter）

#正则中的元字符
#\d
#\w
#\s
#\t
#\n
#\D
#\W
#\S
# . 匹配除了换行符之外的所有
#[^] 非字符组
#^ 匹配字符串开始
#$匹配字符串结尾

# | 或
# （） 约束某个元字符的作用范围

#量词
#{n} 匹配n次
# {n,} 至少n次
# {n,m}至少n次，之多m次
# ？零次或者一次
# + 一次或者多次
# * 零次或者多次

#贪婪匹配  贪心算法 + 回溯算法， 在量词允许范围内，匹配尽量多的内容
   # # .*x 表示匹配任意字符任意长度，但是遇到最后一个x才停下
#非贪懒匹配
   # 原字符 量词 ？
   # .*?x 表示匹配任意字符任意长度，但是遇到x就停下

#转移符号
  #原本有特殊意义的字符，需要表示他原有意义的时候，需要加转义符号
  #对一部分元字符生效，把这个元字符放在字符组里


# findall  取所有符合条件的
   #    按照完整的正则进行匹配，只能现实到括号内匹配到的内容
   #  取消优先显示 （？：  ）

# search  只取第一个满足条件的
  # search 按照完整的正则进行匹配，现实完整的匹配内容，可以通过给group（）方法传参数，来获取具体文组中的内容

import re
# split
# ret = re.split('\d\d\d','asdfa123asdfasf')
# ret = re.split('(\d\d\d)','asdfa123asdfasf')
# print(ret)

# sub
# subn


# match
    #从头着，其余和search一样
# compile
# finditer
  #返回迭代器，节省内存空间
# ret = re.finditer("\d+","adfa234234asf43sdf3")
# for i in ret:
#     print(i.group())


#分组命名
   #（?P<name>RE)
   # ret.group('name')
#分组命名的引用
   # <asdasd>asdfasdfasdfasf42352222@@@@asdf</asdasd>
# exp = '<asdasd>asdfasdfasdfasf42352222@@@@asdf</asdasd>sdfaasdf</asdf>'
# ret = re.compile("<\w+>.*?</\w+>")
# res = ret.search(exp)
# print(res)
#
# ret1 = re.compile("(?P<tag><\w+>).*?(?P=tag)")
# res1 = ret.search(exp)
# print(res1)