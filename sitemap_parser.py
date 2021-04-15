from bs4 import BeautifulSoup
import requests


class SitemapParser:
    def __init__(self):
        self.count = 0

    def find_xml_sitemap(self, url):
        sitemap_list = []
        url = url + 'robots.txt'
        response = requests.get(url).text
        response = response.split('\n')
        sitemap_links = [i for i in response if i[0:7] == 'Sitemap']
        if sitemap_links == []:
            return "Sitemap does not exist"
        else:
            sitemap_links = [i[9:] for i in sitemap_links]
            for i in sitemap_links:
                self.count += 1
                sitemap_list.append(self.parser_sitemap_xml(i))
            return sitemap_list

    def parser_sitemap_xml(self, site):
        try:
            response = requests.get(site).text
            soup = BeautifulSoup(response, 'html.parser')
            urls = soup.find_all('loc')
            list = []
            for url in urls:
                self.count += 1
                url = str(url)
                url = url.replace("<loc>", "").replace("</loc>", "")
                list.append(url)
            return list
        except:
            "Ошибка"

    def url_name_handler(self, url):
        if url[-3:-1] == 'ru':
            url = url[8:-4]
        else:
            url = url[8:-5]
        return url

    def record_txt_file(self, url, sitemap_list):
        try:
            file_name = self.url_name_handler(url)
            file = open("{}.txt".format(file_name), 'w')
            for i in sitemap_list:
                for j in i:
                    file.write("{}\n".format(j))
            file.close()
        except:
            "Ошибка"
