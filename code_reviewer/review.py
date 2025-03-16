# install:
#   pip install click requests python-dotenv -i https://mirrors.cloud.tencent.com/pypi/simple/
# 
# Linux setting:
#   vim ~/.bashrc
#   alias review="python /path/to/your/review.py"
# 
# usage:
#   review -f ./your_code.py
#
# simple usage:
#   python3 review.py -f ./your_code.py


import os
import requests
import click

from dotenv import load_dotenv


# 加载敏感参数
load_dotenv()
langflow_app_id = os.getenv("LANGFLOW_APP_ID").strip()


# 参数
URL = f"http://127.0.0.1:7860/api/v1/run/{langflow_app_id}?stream=false"
HEADERS = {'Content-Type': 'application/json'}


def get_content(file_path):
    if not os.path.exists(file_path):
        print(f"Error: can not find {file_path}")
        return None

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    return content


def review(message, url, headers):
    data = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
        "tweaks": {
            "ChatInput-aYCPq": {},
            "Prompt-RbwEW": {},
            "ChatOutput-KIRYB": {},
            "CustomComponent-vtvSX": {}
        }
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'status_code: {response.status_code}')

    return None


def gen_review(filepath):
    filepath = filepath.strip()
    if not filepath:
        print('You should use -f to specify the file path')

    content = get_content(filepath)
    if content is not None:
        response = review(message=content,
                          url=URL,
                          headers=HEADERS)
        res = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
        return res

    return None


@click.command()
@click.option('-f', '--filepath', required=True, type=click.STRING, help='Specify the file path')
def app(filepath):
    return gen_review(filepath)


if __name__ == '__main__':
    res = app(standalone_mode=False)
    print(f"检查报告出炉的说 (・ω< )★\n\n{res}")
