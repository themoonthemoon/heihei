import pandas as pd
import random

# 正则表达式用于验证手机号
REGEX = r"^\d{11}$"

# 生成100个随机手机号
phones = []
for _ in range(100):
    phone = "1" + "".join(random.choices("0123456789", k=10))
    phones.append(phone)
# 生成随机封禁原因
reasons = [
    "自动检测到异常行为",
    "已停机",
    "号码被黑名单 blocking",
    "短信频率过高",
    "异常操作记录",
]

# 创建数据框并导出为Excel
df = pd.DataFrame(
    {"手机号": phones, "封禁原因": [random.choice(reasons) for _ in range(100)]}
)
df.to_excel("./data/手机号封禁数据.xlsx", index=False)
