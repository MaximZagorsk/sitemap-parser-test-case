from sitemap_parser import SitemapParser
import time
print("Введите URl обязательно в таком формате: https://example.com/")
url = input()
start_time = time.time()
sp = SitemapParser()
url_list = sp.find_xml_sitemap(url)
sp.record_txt_file(url, url_list)
print("--- %s seconds ---" % (time.time() - start_time))
print("{} Ссылок найдено".format(sp.count))


