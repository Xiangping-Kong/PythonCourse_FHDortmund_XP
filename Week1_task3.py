if __name__ == '__main__':
    # 1.整数转浮点数
    num_int = 7
    num_float = float(num_int)
    print("Integer " + str(num_int) + " converted to float: " + str(num_float))

    # 2.浮点数转整数
    float_num = 9.8
    int_from_float = int(float_num)
    print("Float " + str(float_num) + " converted to integer: " + str(int_from_float))

    # 3.整数转字符串
    int_2 = 12
    str_from_int = str(int_2)
    print("Integer " + str(int_2) + " converted to string: " + str(str_from_int))

    # 4.数字字符串转整数
    num_str = "25"
    int_from_str = int(num_str)
    print("String '" + num_str + "' converted to integer: " + str(int_from_str))

    # 5.整数转布尔值
    bool_int = 5
    bool_from_int = bool(bool_int)
    print("Integer " + str(bool_int) + " converted to boolean: " + str(bool_from_int))
