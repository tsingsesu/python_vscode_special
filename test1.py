print ('这是第一次测试')
print ('这是第二次测试')

import sys
import time

def char_generator(text):
    """生成器：逐个产出文字"""
    for char in text:
        yield char

def typewriter_print(text, delay=0.3):
    """使用生成器实现逐字弹出效果"""
    for char in char_generator(text):
        sys.stdout.write(char)
        sys.stdout.flush()  # 立即刷新缓冲区，实现"弹出"效果
        time.sleep(delay)
    print()  # 最后换行

typewriter_print('这是第三次测试')
