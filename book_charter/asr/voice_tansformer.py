import os
import subprocess

# 配置参数
input_folder = "D:/develop/AI/AI-Voice/语音识别微调/微调原始内容/voice"  # 输入文件夹
output_folder = "D:/develop/AI/AI-Voice/语音识别微调/微调原始内容/voice_transformer"  # 输出文件夹
ffmpeg_path = "D:/develop/ffmpeg-7.0.2/bin/ffmpeg.exe"  # ffmpeg可执行文件路径

# 音频转换参数
sample_rate = 16000  # 采样率
channels = 1  # 声道数
bit_depth = 16  # 位深度 (16位 = 2字节)

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有wav文件
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".wav"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 构建ffmpeg命令
        command = [
            ffmpeg_path,
            "-i", input_path,
            "-ar", str(sample_rate),  # 设置采样率
            "-ac", str(channels),  # 设置声道数
            "-sample_fmt", "s16",  # 设置样本格式为16位有符号整数
            "-y",  # 覆盖输出文件而不询问
            output_path
        ]

        # 执行命令
        try:
            subprocess.run(command, check=True)
            print(f"成功转换: {filename}")
        except subprocess.CalledProcessError as e:
            print(f"转换失败: {filename}, 错误: {e}")

print("所有文件转换完成!")