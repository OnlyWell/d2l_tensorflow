import wave
import os
import json
from pathlib import Path


def get_wav_duration(wav_path):
    """计算音频文件的市场"""
    try:
        with wave.open(wav_path, 'rb') as wav_file:
            frames = wav_file.getnframes()
            rate = wav_file.getframerate()
            duration = frames / float(rate)
            return duration
    except Exception as e:
        print(f"Error processing {wav_path}: {str(e)}")
        return None

def calculate_source_len(duration, sample_rate=16000, frame_length_ms=25, frame_shift_ms=10):
    """计算总音频长度"""
    frame_length = frame_length_ms / 1000
    frame_shift = frame_shift_ms / 1000

    # Calculate samples
    samples_per_frame = int(sample_rate * frame_length)
    samples_per_shift = int(sample_rate * frame_shift)
    total_samples = int(duration * sample_rate)

    # Calculate total frames (source_len)
    num_frames = 1 + (total_samples - samples_per_frame) // samples_per_shift
    return num_frames


def process_wav_files(input_dir, output_json):
    """整理输出wave文件的参数"""
    results = []

    if not os.path.exists(input_dir):
        print(f"Directory {input_dir} does not exist.")
        return

    for wav_file in Path(input_dir).glob("*.wav"):
        duration = get_wav_duration(str(wav_file))
        if duration is not None:
            source_len = calculate_source_len(duration)
            # 以funAsr的训练集格式为样本
            entry = {
                "key": wav_file.stem,
                "source": str(wav_file),
                "source_len": source_len,
                "target": "",
                "target_len": 0
            }
            results.append(entry)

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Results saved to {output_json}")


def main():
    input_dir = "D:/develop/AI/AI-Voice/语音识别微调/微调原始内容/voice_transformer"
    output_json = "wav_lengths.json"

    process_wav_files(input_dir, output_json)

if __name__ == "__main__":
    main()