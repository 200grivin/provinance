def func1(arg1, arg2):
    var6 = func2(arg1, arg2)
    var7 = func6()
    def func7(arg8, arg9):
        var10 = var7 - var6
        var11 = var6 & var10
        var12 = (arg2 & var11 - -363614767) & arg9
        var13 = var12 + var12
        var14 = var12 ^ ((var11 + 2027815807) - arg9)
        var15 = arg8 | arg8
        var16 = arg2 - var13 & arg1 | var12
        var17 = var7 + var13
        var18 = arg8 & var12 | arg9 & var15
        var19 = (var12 - arg1 ^ var12) ^ var13
        var20 = var16 | var12 & var10 | arg8
        var21 = var17 + var11
        var22 = (var17 & arg1 ^ arg8) | -1846154341
        var23 = -492 & (arg9 ^ arg8 | var14)
        result = (-522 + (var12 ^ var17 ^ (-1756638647 + (var14 & arg1)) ^ var20 + (var18 + arg9) - var23) | arg8) + var21
        return result
    var24 = func7(var7, var6)
    var25 = func10()
    var26 = var7 - -693
    var27 = -645571005 - arg2 & var6 & (var25 - var24) - var7 + var6 | 1771007078 & (arg2 & var6 - arg1 - var24 + arg2 | var7 + (var24 | var26)) + (((arg2 ^ -1023758499) & var24 + arg2) ^ arg1) - var26
    var28 = var26 - var7 | 2082525773
    result = var25 & var7 ^ var28
    return result
def func10():
    func8()
    result = len((((2 & i) & i) | -9 ^ -7 for i in range(50)))
    func9()
    return result
def func9():
    global len
    del len
def func8():
    global len
    len = lambda x : 3
def func6():
    func4()
    result = len(xrange(3))
    func5()
    return result
def func5():
    global len
    del len
def func4():
    global len
    len = lambda x : -2
def func2(arg3, arg4):
    closure = [0]
    def func3(acc, rest):
        var5 = -3 | ((acc & -1 - -9 + rest) | 4 | acc)
        closure[0] += var5
        if acc == 0:
            return var5
        else:
            result = func3(acc - 1, var5)
            return result
    result = func3(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 29'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
