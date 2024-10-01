import pandas as pd
import matplotlib.pyplot as plt

# 使用原始字符串来指定CSV文件路径
csv_file_path = r'E:/vscode/perfectworldmajor/cagogo.csv'

# 读取CSV文件
df = pd.read_csv(csv_file_path)

# 将日期转换为日期时间对象
df['date'] = pd.to_datetime(df['date'])

# 将name列转换为字符串类型
df['name'] = df['name'].astype(str)

# 创建一个折线图
plt.figure(figsize=(10, 6))
plt.plot(df['name'], df['date'])

# 设置图形标题和坐标轴标签
plt.title('Dates and Names')
plt.xlabel('Name')
plt.ylabel('Date')

# 显示图形
plt.show()
