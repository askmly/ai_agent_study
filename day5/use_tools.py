# use_tools.py
# 这个文件导入并使用 my_tools 模块中的函数

# 导入方式1：from my_tools import 函数名1, 函数名2, ...
# 这样可以直接用函数名，不需要加模块名前缀
from my_tools import is_even, sum_to, add, divide, print_mul_table

# 导入方式2：import 模块名
# 这样要用 模块名.函数名 来调用
import my_tools

# === 使用 from...import 导入的函数（直接调用） ===
print("=== from...import 方式 ===")
print(f"is_even(4) = {is_even(4)}")        # True
print(f"sum_to(100) = {sum_to(100)}")      # 5050
print(f"add(3, 5) = {add(3, 5)}")          # 8
print(f"divide(10, 3) = {divide(10, 3)}")  # 3.333...
print(f"divide(10, 0) = {divide(10, 0)}")  # 错误提示

print("\n--- 3的乘法表 ---")
print_mul_table(3)

# === 使用 import 模块名 方式 ===
print("\n=== import 模块名 方式 ===")
print(f"my_tools.is_even(7) = {my_tools.is_even(7)}")
print(f"my_tools.sum_to(50) = {my_tools.sum_to(50)}")
print(f"my_tools.divide(20, 4) = {my_tools.divide(20, 4)}")

print("\n--- 5的乘法表 ---")
my_tools.print_mul_table(5)