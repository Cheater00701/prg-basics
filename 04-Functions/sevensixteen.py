def f(n):
    val1 = 0
    val2 = 1
    result = 0
    for i in range(n - 2):
        result = val1 + val2
        val1 = val2
        val2 = result
    return result