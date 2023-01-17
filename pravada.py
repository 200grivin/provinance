def func1(arg1, arg2):
    def func2(arg3, arg4):
        def func3(arg5, arg6):
            var17 = var9(arg1, arg6)
            var21 = func7(arg6, arg5)
            result = arg2 | (arg6 + (arg4 + 75890132) ^ -99 + arg1 ^ (arg6 - 271 + var21 - arg1 - arg4)) + var17
            return result
        var22 = func3(arg1, arg3)
        var23 = (-71 + -345) - arg4 + -588764744
        var24 = arg2 - var23
        var25 = arg3 & 784
        var26 = (var23 & var23) + var23 | var25
        var27 = var24 - arg4 + arg3 + var24
        var28 = var26 + arg4 | -784
        var29 = arg2 - var24 ^ var22 - var23
        var30 = var27 + ((162289918 & arg1) - var25)
        var31 = arg4 - var27 + arg1 | arg3
        var32 = var30 | var30 - var24 + arg4
        if var32 < var23:
            var33 = (var32 ^ -675512366 | arg1) + var32
        else:
            var33 = arg1 | var25
        var34 = var28 & var30
        var35 = (-158444562 | var26 & var22) & var28
        if var29 < arg4:
            var36 = (var22 | (arg4 + var35)) + arg4
        else:
            var36 = (arg3 | arg3 ^ var23) & arg2
        var37 = var30 - var29
        var38 = var24 + var29
        var39 = (var35 | var30) - arg2 + arg2
        result = var34 ^ var31
        return result
    var40 = func2(arg2, arg1)
    var45 = func9(arg2, arg1)
    var46 = var40 - (arg1 - var45 & ((429 & arg1) | var40 | var40)) & var40 - arg2 & arg1
    var47 = var45 & var40
    result = 655 | arg2
    return result
def func9(arg41, arg42):
    var43 = 0
    for var44 in range(2):
        var43 += var44 + 7 + -8
    return var43
def func6(arg10, arg11):
    if arg10 < arg10:
        var12 = ((arg11 - (686 + -1483337195 + -166 - -778) + (-1684742897 ^ (-2052001531 ^ arg11 + (arg11 & arg10 | 772167209 - 857 - 939 ^ arg10 | arg11)) + arg11)) & -151 + (arg11 | arg10)) + 207
    else:
        var12 = -1885855557 + (-1449315153 & 2110918617) + ((2115456645 | arg11 - arg11) ^ arg11 | 1083531727) | -1136798540
    var13 = 462 - arg11 | ((-108 | (arg11 - arg10 + (1258308047 & -1923876006 | arg11 + -768860082))) & arg11) ^ arg11
    var14 = (1854848030 & ((arg11 ^ 556 + arg10 ^ -1174680712 + ((var13 ^ -1887962453 ^ -591777884 ^ (var13 & -40379691 | -430 - arg10) ^ arg10 | 654 & var13) ^ 439) & 1366089860 ^ var13 | 243184249) - 193)) - arg11 + arg11
    var15 = (((77 ^ 824 ^ var14 & var14) - -647618010) & var14) ^ (var14 ^ 31 - (37003794 & arg11 | var13 - var14 ^ arg11 + -411 - var13)) + (arg10 - arg10 ^ (arg10 - (var14 | arg10 | -703540477)) ^ arg11)
    var16 = var14 & (var15 + (arg11 - -633743100) | var14 | -1188106740 & -874)
    result = (var16 ^ var15 | arg10 | (var15 - (var15 & arg11)) & (var14 & ((var13 | var15) - arg11)) + var14) | arg10
    return result
def func5():
    closure = [6]
    def func4(arg7, arg8):
        closure[0] += func6(arg7, arg8)
        return closure[0]
    func = func4
    return func
var9 = func5()
def func7(arg18, arg19):
    def func8(acc, rest):
        var20 = acc - -8 & -10
        if acc == 0:
            return var20
        else:
            result = func8(acc - 1, var20)
            return result
    result = func8(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 10'
    print 'arg_number: 48'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
