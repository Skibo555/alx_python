def multiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda x, y, z = [] : x * z + y * z, my_list, number,))
    return new_list