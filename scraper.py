from selenium import webdriver

browser = webdriver.Chrome(executable_path="/home/lea/chromedriver")
browser.get("https://www.bbcgoodfood.com/search/recipes/page/2/?q=Low-sugar+breakfast+recipes&sort=-relevance")


for page in range(1, 5, 1):
    browser.get("https://www.bbcgoodfood.com/search/recipes/page/{}/?q=Low-sugar+breakfast+recipes&sort=-relevance".format(page))
    for i in range(1, 5, 1):
        element = browser.find_element_by_xpath('//*[@id="main-content"]/form/div/div[4]/div[1]/div[1]/div/div[{}]/div/div[2]/div[1]/h4/a'.format(i))
        href = element.get_attribute('href')
        print(href)
