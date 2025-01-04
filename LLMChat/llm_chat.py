import os
import hashlib

conversation_base = [
    {"role": "user", "content": "次で入力する文章を要約してください。出力時は丁寧な日本語で回答してください。"},
    {"role": "assistant", "content": "次の入力を待機します。"}
]


def main():
    input_folder = 'LLMChat/input'
    output_folder = 'LLMChat/output'
    
    # inputフォルダにある全ての*.txtファイルを読み込む
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_folder, filename)
            with open(input_path, 'r', encoding='utf-8') as f:
                text = f.read()
                
            # 読み込んだテキストをmock関数へ渡し、文字列を受け取る
            llm_response = request_llm(text)
            
            # outputフォルダにファイル名の先頭にoutput_を付けて書き込む
            output_filename = 'output_' + filename
            output_path = os.path.join(output_folder, output_filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(llm_response)

def request_llm(user_input):
    conversation = conversation_base.copy()
    conversation.append({"role": "user", "content": user_input})

    print(conversation)

    # Request API の引数に prompt を設定する
    prompt = conversation_to_prompt(conversation)
    # mock はリクエスト処理に変更
    response = mock(prompt)

    return response


def conversation_to_prompt(conversation):
    prompt = ""
    for message in conversation:
        prompt += f"{message['role']}: {message['content']}\n"
    return prompt

def mock(text):
    # 受け取った文字列のSHA-256のハッシュ値を返す
    sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return sha256_hash


if __name__ == '__main__':
    main()
