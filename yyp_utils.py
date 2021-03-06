#coding: utf8

__author__ = 'liangguanhui@qq.com'


import StringIO
from yyp_exception import YYPException

def readfull(fd, size):
    total = None
    remain = size
    while True:
        buf = fd.read(remain)
        if not buf:
            raise YYPException("Can not readfull for size %s, remain %s. Maybe it has shutdown." % (size, remain))
        rl = len(buf)
        #print "read size %s, return %s" % (size, rl)
        assert rl <= remain
        remain -= rl
        if remain <= 0:
            if total is None:
                # total = None 表示第一次读取即能够读取足够的数据
                return buf
            else:
                total.write(buf)
                return total.getvalues()
        # 到达这里表示不能第一次读取足够数据，需要使用buffer缓存起来
        if total is None:
            total = StringIO.StringIO()
        total.write(buf)

def str2intip(s):
    p = s.split(".")
    if len(p) != 4:
        return False, 0

    ip = 0
    for i, s in enumerate(p):
        if not s.isdigit():
            return False, 0
        n = int(s)
        if n < 0 or n > 255:
            return False, 0
        ip += n * (256 ** i)

    return True, ip