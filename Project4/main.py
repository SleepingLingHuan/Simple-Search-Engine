import pynlpir
from pathlib import Path
import tkinter as tk
ENCODE='utf-8'
def build_index(mypath):
    index = {}
    def file_split(content, file_path):
        offset = 0
        mylist = pynlpir.segment(content, pos_tagging=False)
        for word in mylist:
            if word != '':
                if word not in index:
                    index[word] = {file_path: [offset]}
                else:
                    if file_path not in index[word]:
                        index[word][file_path]=[offset]
                    else:
                        index[word][file_path]=[offset]
                offset+=len(word.encode(ENCODE))

    def get_files():
        pynlpir.open()
        for file_path in Path(mypath).rglob('*'):
            if file_path.is_file():
                print(file_path.relative_to(mypath))
                with open(file_path, 'r', encoding=ENCODE, errors='ignore') as file:
                    content =file.read().replace('\n','').replace(' ', '').replace('\t', '')
                    file_split(content, str(file_path.relative_to(mypath)))
        pynlpir.close()
    get_files()
    return index

#查找内容
def search_index(search_str, index):
    result = {}  # {file_path: {count, offsets[]}}
    pynlpir.open()
    mylist = pynlpir.segment(search_str, pos_tagging=False)

    for word in mylist:
        if word in index:
            for file_path, offsets in index[word].items():
                result[file_path] = result.get(file_path, {'count': 0, 'offsets': []})
                result[file_path]['count'] += len(offsets)
                result[file_path]['offsets'].extend(offsets)

    sorted_results = sorted(result.items(), key=lambda x: x[1]['count'], reverse=True)
    pynlpir.close()
    return sorted_results
#显示查找内容
def display_info():
    search_str = entry_search_str.get()
    result = search_index(search_str, index)
    text_info.delete('1.0', tk.END)
    for file_path, info in result:
        text_info.insert(tk.END, mypath+'\\'+file_path + '\n')
        with open(mypath+'\\'+file_path, 'r', encoding=ENCODE, errors='ignore') as file:
            for line_number, line in enumerate(file, start=1):
                for line_number, line in enumerate(file, start=1):
                    if "【 标  题 】" in line:
                        text_info.insert(tk.END, line.strip() + '\n')  # 标题行
                        break
            count = 0
            num = 1
            for every_offset in info['offsets']:
                file.seek(every_offset)
                text_info.insert(tk.END, file.read(60).replace('\n', '') + '\n\n')  # 文本内容
                count += 1
                if count == 2:
                    break

#显示全文
def display_all():
    file_path=entry_path.get()
    with open(file_path, 'r', encoding=ENCODE,errors='ignore') as file:
        text_info.delete('1.0', tk.END)
        text_info.insert(tk.END, file.read())

#主函数
mypath=r"E:\数据结构课程设计\Problem4\data"
index=build_index(mypath)
file_path = r"E:\数据结构课程设计\Problem4\text.txt"
#输出分词引索到文件中
with open(file_path, 'w+', encoding=ENCODE) as data:
    for word, documents in index.items():
        print(f"{word}: {documents}", file=data)

#可视化
app=tk.Tk()
app.title("搜索引擎")
tk.Label(app,text="搜索内容").pack()
entry_search_str=tk.Entry(app)
entry_search_str.pack()
button_read=tk.Button(app,text="点击搜索",command=display_info)
button_read.pack()
tk.Label(app,text="文件对应路径").pack()
entry_path=tk.Entry(app)
entry_path.pack()
button_show=tk.Button(app,text="全文展示",command=display_all)
button_show.pack()
text_info = tk.Text(app)
text_info.pack()
button_exit = tk.Button(app, text="退出", command=app.quit)
button_exit.pack()
app.mainloop()