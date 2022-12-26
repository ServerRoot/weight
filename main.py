#coding:utf-8
import requests
import argparse
import json

f = open("config.json","r",encoding="utf-8")
key = json.load(f)

file_title = ['Url', '百度权重', '移动权重']

with open('1.csv', "a+") as csv_file:
    csv_file.seek(0)
    if not "百度权重" in csv_file.read():
        csv_file.write("\t\t".join(file_title) + "\n")

def get_data(url):
    try:
        bdQZ = f"https://apistore.aizhan.com/baidurank/siteinfos/[{key['key']}]?domains={url}"
        res = requests.get(bdQZ).json()
        for data in res["data"]["success"]:
            with open('1.csv', "a") as csv_file:
                csv_file.write(f"{data['domain']}\t\t{data['pc_br']}\t\t{data['m_br']}\n")
            print("[+]", data['domain'], "查询成功!")
    except BaseException as FError:
        print("[-] " ,FError)
        with open("errlog.txt",'a',encoding="utf-8") as ferr:
            ferr.write(FError+"\n")

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--u",type=str,help="指定域名查询")
    parser.add_argument("-f","--f",type=str,help="指定文件查询")
    arg = parser.parse_args()
    return arg

def main():
    print(r"""
                   .__       .__     __   
    __  _  __ ____ |__| ____ |  |___/  |_ 
    \ \/ \/ // __ \|  |/ ___\|  |  \   __\
     \     /\  ___/|  / /_/  >   Y  \  |  
      \/\_/  \___  >__\___  /|___|  /__|  
                 \/  /_____/      \/    
                   
                                版本:1.1.1.1
                                作者:tutu
    """)
    url = args().u
    file = args().f
    app = args().easter
    if url:
        bdQZ = f"https://apistore.aizhan.com/baidurank/siteinfos/[{key['key']}]?domains={url}"
        res = requests.get(url=bdQZ).json()
        print("[+]",res["data"]["success"][0]["domain"],"--->","百度权重:",res["data"]["success"][0]["pc_br"],"移动权重:",res["data"]["success"][0]["m_br"])
    elif file:
        with open(file, encoding="utf-8") as f:
            urls = ""
            for index, url in enumerate(f.readlines()):
                urls += f'{url.split("/")[2]}|'
                if index % 50 == 49:
                    get_data(url=urls)
                    urls = ""
            get_data(url=urls)
    elif app:
        happy()
    else:
        print("参数不合法!")
        exit()

if __name__ == '__main__':
    main()