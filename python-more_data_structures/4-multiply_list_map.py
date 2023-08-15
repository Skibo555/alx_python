def multiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda x, y, : x*4 + y*4, my_list, number,))
    return new_list