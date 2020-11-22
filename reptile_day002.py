import requests
import json


# 1.解析真实地址抓取
link="""https://api-zero.livere.com/v1/comments/list?callback=jQuery112407673461727809291_1606031206111&limit=10&repSeq=4272904&requestPath=/v1/comments/list&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1606031206113"""
headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/65.0'
    }
r=requests.get(link,headers=headers)
print(r.text)

# # 2.使用json库解析数据

def single_page_comment(link):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/65.0'
    }
    r = requests.get(link, headers=headers)
    json_string = r.text
    json_string = json_string[json_string.find('{'):-2]  # 从第一个左大括号提取，最后的两个字符 - 括号和分号不取
    json_data = json.loads(json_string)
    comment_list = json_data['results']['parents']

    for eachone in comment_list:
        message = eachone['content']
        print(message)


for page in range(1, 4):
    link1 = 'https://api-zero.livere.com/v1/comments/list?callback=jQuery112403763219873362794_1606033887393&limit=10&offset='
    link2 = '&repSeq=4272904&requestPath=/v1/comments/list&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1606033887395'
    page_str = str(page)
    link = link1 + page_str + link2
    print(link)
    single_page_comment(link)
