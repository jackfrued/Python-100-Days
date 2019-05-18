"""
Author: Tang

Date: 2019-0518

设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

"""
import random

def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """

    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    gen_code = ''

    for _ in range(code_len):
        gen_code += random.choice(all_chars)
    return gen_code



if __name__ == "__main__":
    code = generate_code()
    print("Code: {}".format(code))
