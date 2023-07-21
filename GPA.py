import pandas as pd
data = [
    {"class": "高等数学（上）A", "score": 90, "credit": 4},
    {"class": "高等数学（下）A", "score": 90, "credit": 4},
    {"class": "线性代数", "score": 90, "credit": 4},
    {"class": "大学物理 B（上）", "score": 90, "credit": 4},
    {"class": "大学物理 B（下）", "score": 90, "credit": 4},
    {"class": "计算机程序设计基础A", "score": 90, "credit": 3},
    {"class": "概率论与数理统计", "score": 90, "credit": 3},
    {"class": "离散数学", "score": 90, "credit": 3},
    {"class": "数据结构与算法分析", "score": 90, "credit": 3},
    {"class": "计算机组成原理", "score": 90, "credit": 3},
    {"class": "数字逻辑", "score": 90, "credit": 3},
    {"class": "算法设计与分析", "score": 90, "credit": 3},
    {"class": "数据库原理", "score": 90, "credit": 3},
    {"class": "人工智能", "score": 90, "credit": 3},
    {"class": "计算机网络", "score": 90, "credit": 3},
    {"class": "计算机操作系统", "score": 90, "credit": 3},
    {"class": "软件工程", "score": 90, "credit": 3},
    {"class": "创新实践I", "score": 90, "credit": 2},
    {"class": "创新实践II", "score": 90, "credit": 2},
]

def compute(G):
    return 4 - (3 * (100 - G) ** 2) / 1600

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Calculate GPA and contribute for each course using apply
df['GPA'] = df['score'].apply(compute)
df['contribute'] = df['GPA'] * df['credit']

# Print results
sum_credit = df['credit'].sum()
sum_contribute = df['contribute'].sum()

print("sum_credit:", sum_credit)
print("sum_contribute:", sum_contribute)

# Format and print course data
for _, row in df.iterrows():
    print("{} credit：{} score：{} gpa：{} contribution：{}".format(
        row['class'], row['credit'], row['score'], row['GPA'], row['contribute']
    ))

print("avggpa:", sum_contribute / sum_credit)


