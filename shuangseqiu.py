import requests
from lxml import etree
import json
import random


# from urllib.request import urlopen

class Shuangseqiu:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
        # self.url_temp = 'http://datachart.500.com/dlt/?expect=all&from=20011&to=20015'

    def parser_url(self, url):
        response = requests.get(url, headers=self.headers)
        # return response.content.decode(encoding= 'gbk')
        return response.content.decode()

    def get_content_list(self, html_str):  # 提取数据
        html = etree.HTML(html_str)
        # content_list = []
        qianqu_list = html.xpath("//tr/td[@class='chartBall01']/text()")
        houqu_list = html.xpath("//td[@class='chartBall02']/text()")
        qishu_list = []
        xuanhao_list = []
        # td_list = html.xpath("//tr/td[@align='center']")
        # print(td_list)
        # for td in td_list:
        qihao_list = html.xpath("//td[@align='center']/text()")
        for qihao in qihao_list:
            if qihao.strip().isdigit() is True:
                qishu_list.append(qihao.replace(' ', ''))

        for i in range(len(qishu_list)):
            xuanhao_list.append(qianqu_list[(i * 6):(i + 1) * 6] + houqu_list[(i ):(i + 1)])
        # qianqu_list.append(html.xpath("//tr/td[@class='chartBall01']/text()"))
        # houqu_list.append(html.xpath("//td[@class='chartBall02']/text()"))

        # item = {"qishu": qishu_list, "qianqu": qianqu_list, "houqu": houqu_list}

        # content_list.append(item)
        # return content_list
        return xuanhao_list

    def save_content_list(self, content_list):
        with open('shuangse.txt', 'w', encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write('\n')

    def zixuanhao(self):
        zixuan_qian = random.sample(range(1, 34), 6)
        zixuan_qian.sort()
        zixuan_hou = random.sample(range(1, 17), 1)
        zixuan = zixuan_qian + zixuan_hou
        return zixuan

    def run(self):
        url = 'http://datachart.500.com/ssq/zoushi/newinc/jbzs_redblue.php?expect=all&from=03001&to=20020'
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
    letou = Shuangseqiu()
    for h in range(5):
        letou.run()
