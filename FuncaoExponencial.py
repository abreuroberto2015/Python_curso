def func_exponecial(base_num, exp_num):
    result = 1
    for index in range(exp_num):
        result = result * base_num        
    return result
    
print (func_exponecial(3, 4))