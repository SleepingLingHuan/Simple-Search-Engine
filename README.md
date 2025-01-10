# Simple-Search-Engine
/**
 * @copyright
 * Project: Data Structure Course Design Project 4, Simple-Search-Engine
 * Course: Data Structure (2024)
 * Institution: School of Computer Science, China University of Geosciences (Wuhan)
 * Major: Software Engineering
 * Author: Ge Xuanyu
 * Date: January 10, 2025
 * 
 * All rights reserved. This project is for educational purposes only and may not be used, distributed, or modified without explicit permission from the author and the institution.
 *
 * @版权声明
 * 项目名称：数据结构课程设计项目4，简单搜索引擎
 * 课程名称：数据结构（2024年）
 * 所属学院：中国地质大学（武汉）计算机学院
 * 专业：软件工程
 * 作者：葛轩宇
 * 日期：2025年1月10日
 * 
 * 版权所有。本项目仅限于教育用途，未经作者及所属学院明确许可，不得用于其他用途、分发或修改。

 */

 这是一个由Python构建的简单搜索引擎，可读取本地文件夹中的多个.txt文本的内容并进行内容搜索，无联网功能。主要基于pynlpir和tkinter库实现。  
文件夹“data”和“tc-corpus-answer”中的内容都是测试数据，可在main.py中修改mypath路径来选定搜索引擎的目标文件夹。需要注意的是，文件夹“data”中的数据是“UTF-8”编码，文件夹“tc-corpus-answer”中的数据是“GB-2312”编码，更改文件夹时需修改程序中的ENCODE变量。由于我仅能在该项目中上传不多于100个文件，因此我无法上传全部数据集，你可以通过该链接下载全部数据集。测试数据：http://www.nlpir.org/wordpress/download/tc-corpus-answer.rar  
运行程序后，在文本框中输入需要搜索的词，点击“搜索”按钮后可搜索并展示全部含有目标词的文本路径及其部分内容。复制文本路径到下方文本框，点击“全文展示”按钮可显示对应文本的全部内容。  

This is a simple search engine built with Python. It can read the contents of multiple `.txt` files from a local folder and perform content searches without requiring an internet connection. The project is primarily implemented using the `pynlpir` and `tkinter` libraries.

The folders "data" and "tc-corpus-answer" contain test data. You can change the target folder for the search engine by modifying the `mypath` variable in `main.py`. Note that the files in the "data" folder are encoded in "UTF-8", while the files in the "tc-corpus-answer" folder are encoded in "GB-2312". When switching folders, make sure to update the `ENCODE` variable in the program accordingly. Since I can only upload no more than 100 files in this project, I am unable to upload the entire dataset. You can download the full dataset via this link: Test data: http://www.nlpir.org/wordpress/download/tc-corpus-answer.rar

After running the program, you can enter the keyword you want to search for in the text box and click the "Search" button. The program will display all the file paths containing the target word, along with partial content from those files. To view the full content of a file, copy its file path into the text box below and click the "Display Full Content" button.
