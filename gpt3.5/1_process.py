import json
import random

def transform_jsonl(input_file_path, output_file_path):
    entries = []
    with open(input_file_path, 'r') as file:
        for line in file:
            entry = json.loads(line)
            entries.append(entry)

    # 随机抽取100个条目
    sampled_entries = random.sample(entries, 200)

    with open(output_file_path, 'w') as outfile:
        for entry in sampled_entries:
            messages = []
            messages.append({"role": "system", "content": "You are an helpful assistant"})
            user_message = {"role": "user", "content": entry["questions"]}
            assistant_message = {"role": "assistant", "content": entry["answers"]}
            messages.extend([user_message, assistant_message])
            result = {"messages": messages}
            json.dump(result, outfile, ensure_ascii=False)
            outfile.write('\n')

input_file_path = '\A:\Desktop\AI Training\Datasets\dolly15k\databricks-dolly-15k.jsonl' # 请替换为您的输入JSONL文件路径
output_file_path = '\A:\Desktop\AI Training\Datasets\dolly15k\output.jsonl' # 请替换为您想要保存的输出JSONL文件路径
transform_jsonl(input_file_path, output_file_path)
