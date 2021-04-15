from sitemap_parser import SitemapParser

print("Введите URl обязательно в таком формате: https://example.com/")
url = input()
sp = SitemapParser()
url_list = sp.find_xml_sitemap(url)
sp.record_txt_file(url, url_list)
print("{} Ссылок найдено".format(sp.count))


