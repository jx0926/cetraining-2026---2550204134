def calculate_average(numbers):
    """计算一个数字列表的平均值"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# 简单测试（可选）
if __name__ == "__main__":
    test_list = [10, 20, 30, 40, 50]
    print(f"平均值是：{calculate_average(test_list)}")