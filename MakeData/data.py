import pandas as pd
import random


# 生成随机的手机号
def generate_phone_number():
    return "1" + "".join([str(random.randint(0, 9)) for _ in range(10)])


# 封禁原因列表
ban_reasons = ["恶意刷单", "发布违规内容", "账号异常", "欺诈行为", "多次投诉"]

# 生成数据
data = {
    "手机号": [generate_phone_number() for _ in range(100)],  # 生成100个手机号
    "封禁原因": [random.choice(ban_reasons) for _ in range(100)],  # 随机选择封禁原因
}

# 创建DataFrame
df = pd.DataFrame(data)

# 保存为Excel文件
df.to_excel("封禁数据.xlsx", index=False)
print("数据已生成并保存为 '封禁数据.xlsx'")
