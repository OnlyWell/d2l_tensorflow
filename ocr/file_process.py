'''
    将D:\develop\项目\longway\简易知识库\法律法规txt 中的文件每50个一组放到1个新文件夹,
    新文件夹的路径放在D:\develop\项目\longway\简易知识库\ 下,新文件夹命名为法律法规txt1  法律法规txt2 ...
'''
import os
import shutil

import os
import shutil

# 源文件夹路径
source_dir = r'D:\develop\项目\longway\简易知识库\法律法规txt'
# 目标文件夹路径
target_dir = r'D:\develop\项目\longway\简易知识库'

# 获取源文件夹中的所有文件
files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

# 每50个文件一组
group_size = 50
for i in range(0, len(files), group_size):
    # 创建新文件夹
    group_folder = os.path.join(target_dir, f'法律法规txt{i // group_size + 1}')
    os.makedirs(group_folder, exist_ok=True)

    # 将文件移动到新文件夹
    for file in files[i:i + group_size]:
        shutil.move(os.path.join(source_dir, file), os.path.join(group_folder, file))

print("文件分组完成！")

