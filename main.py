# -*- coding: utf-8 -*-
import time
import os

def main():
    """
    这是将被外部包装器脚本调用的主函数。
    它会打印一些信息来表明自己被成功执行了。
    """
    print("**************************************************")
    print("* *")
    print("* 测试程序 main.py 中的 main() 函数成功执行！   *")
    print("* Test program main.py's main() executed successfully!*")
    print("* *")
    print("**************************************************")

    # 打印一些额外信息，证明它确实在运行
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n当前时间 (打印自 {__file__}): {current_time}")

    current_working_dir = os.getcwd()
    print(f"当前工作目录 (打印自 {__file__}): {current_working_dir}")

    print("\n简单测试执行完毕。")

# 这个部分使得你可以直接运行 `python main.py` 来测试这个文件本身
if __name__ == '__main__':
    print(f"直接运行测试文件: {__file__} ...")
    main()
    print(f"测试文件 {__file__} 直接运行结束。")