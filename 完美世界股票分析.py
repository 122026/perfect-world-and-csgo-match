import pandas as pd  
import matplotlib.pyplot as plt  # type: ignore  

# 指定CSV文件路径  
csv_file_path = r"C:\Users\30501\Desktop\perfect world.csv"  # 替换为您的CSV文件路径  

# 使用Pandas的read_csv函数读取CSV文件，并将结果存储在df变量中  
df = pd.read_csv(csv_file_path)  

# 获取用户输入的日期范围  
start_time = input("请输入开始日期（格式：YYYY-MM-DD）：")  
end_time = input("请输入结束日期（格式：YYYY-MM-DD）：")  

# 使用条件筛选数据  
mask = (df['time'] >= start_time) & (df['time'] <= end_time)  
df_range = df.loc[mask]  

# 打印筛选后的数据  
print("筛选后的数据:")  
print(df_range)  

# 打印前五行数据  
print("原数据的前五行:")  
print(df.head())  

# 5、查一下每列的数据类型  
print("数据类型:")  
print(df.dtypes)  

# 6、检测数据集的几行几列（形状）  
print("数据集形状:")  
print(df.shape)  

# 7、获取数据集的长度  
print("数据集长度:")  
print(len(df))  

# 8、获取数据集的基本信息  
print("数据集基本信息:")  
print(df.info())  

# 2.1、检测是否有缺失值  
print("是否有缺失值:")  
print(df.isnull().any())  

# 计算 'high' 和 'low' 列的差值，并将其添加到 DataFrame 中作为新的一列 'diff'  
df_range['diff'] = df_range['high'] - df_range['low']  # 使用筛选后的数据  

# 对 'diff' 列进行分组，并计算每个平台的全球销售差额  
df1 = df_range.groupby('time')['diff'].sum()  # 使用筛选后的数据  

# 打印每个平台的差额  
print("每个平台的差额:")  
print(df1)  

# 绘制线性图  
df1.plot(kind='line', xlabel='time', ylabel='total diff')  
plt.title('Total Diff Over Time (Filtered)')  
plt.xticks(rotation=45)  # 旋转x轴标签以便更好地显示  
plt.tight_layout()  # 自动调整布局以避免重叠  
plt.show()  

# 计算每列（除了'time'列）的最高点和最低点  
for col in df_range.columns:  
    if col not in ['time']:  
        max_value = df_range[col].max()  
        min_value = df_range[col].min()  
        print(f"列 {col}: 最大值 = {max_value}, 最小值 = {min_value}")  

# 创建一个新的DataFrame来存储每列的最高点和最低点  
max_min_df = pd.DataFrame(columns=['Column', 'Max', 'Min'])  

# 将每列的最高点和最低点添加到新的DataFrame中  
for col in df_range.columns:  
    if col not in ['time']:  
        max_value = df_range[col].max()  
        min_value = df_range[col].min()  
        max_min_df = max_min_df.append({'Column': col, 'Max': max_value, 'Min': min_value}, ignore_index=True)  

# 打印新的DataFrame  
print("每列的最大值和最小值:")  
print(max_min_df)  

# 使用matplotlib绘制线性图  
plt.figure(figsize=(10, 6))  
for index, row in max_min_df.iterrows():  
    plt.plot([row['Max'], row['Min']], [index, index], marker='o', color='b')  

plt.xlabel('Value')  
plt.ylabel('Column')  
plt.title('Maximum and Minimum Values for Each Column (Filtered)')  
plt.xticks(range(int(max_min_df['Min'].min()), int(max_min_df['Max'].max()) + 1))  
plt.yticks(range(len(max_min_df)), max_min_df['Column'])  

# 显示图形  
plt.show()
