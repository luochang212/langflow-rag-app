# usage:
#   python review_all.py


import os

import review


def find_files_by_suffix(directory, suffix):
    """查找路径下所有指定后缀的文件列表"""
    if not os.path.exists(directory):
        print(f"Error: can not find {directory}")
        return []
    result = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(suffix):
                result.append(os.path.join(root, file))
    return result


def write_content_to_file(content, save_dir, filename):
    """将内容写入指定目录"""
    if not os.path.exists(save_dir):
        raise Exception('save dir is not exists')

    fn, _ = os.path.splitext(filename)
    file_path = os.path.join(save_dir, fn + '.md')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def app(target_dir, suffix='.py', save_dir='./review/'):
    target_dir = target_dir
    save_dir = save_dir
    files = find_files_by_suffix(directory=target_dir,
                                 suffix=suffix)
    if files:
        for fp in files:
            content = review.gen_review(fp)
            filename = os.path.basename(fp)
            filename = f'review_{filename}'
            write_content_to_file(content, save_dir, filename)


if __name__ == '__main__':
    app(target_dir='./',
        suffix='.py',
        save_dir='./review/')
