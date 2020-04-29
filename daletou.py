import requests
from lxml import etree
import json
import random
import time




class Daletou:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
        

    def parser_url(self, url):
        response = requests.get(url, headers=self.headers)
        
        return response.content.decode()

    def get_content_list(self, html_str):  # 提取数据
        html = etree.HTML(html_str)
        
        qianqu_list = html.xpath("//tr/td[@class='chartBall01']/text()")
        houqu_list = html.xpath("//td[@class='chartBall02']/text()")
        qishu_list = []
        xuanhao_list = []
        
        qihao_list = html.xpath("//td[@align='center']/text()")
        for qihao in qihao_list:
            if qihao.strip().isdigit() is True:
                qishu_list.append(qihao.replace(' ', ''))

        for i in range(len(qishu_list)):
            xuanhao_list.append(qianqu_list[(i * 5):(i + 1) * 5] + houqu_list[(i * 2):(i + 1) * 2])
       
        return xuanhao_list

    def save_content_list(self, content_list):
        with open('dale.txt', 'w', encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write('\n')

    def zixuanhao(self):

        zixuan_qian = random.sample(range(1, 36), 5)
        zixuan_qian.sort()
        zixuan_hou = random.sample(range(1, 13), 2)
        zixuan_hou.sort()
        zixuan = zixuan_qian + zixuan_hou
        return zixuan

    def run(self):
        url = 'http://datachart.500.com/dlt/zoushi/newinc/jbzs_foreback.php?expect=all&from=07001&to=20021'#需手动修改期号范围
        # 发送请求，获取响应

        html_str = self.parser_url(url)



        # 提取数据
        content_list = self.get_content_list(html_str)



        # 保存数据
        self.save_content_list(content_list)

        shuaixuan = self.zixuanhao()

        if shuaixuan in content_list:
            return
        return print(shuaixuan)


if __name__ == '__main__':
    letou = Daletou()
    #生成5组随机选号
    for h in range(5):
        letou.run()
    time.sleep(10)
