import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
from selenium.webdriver.common.keys import Keys
class ExampleSpider(scrapy.Spider):
    name = 'example'

    def start_requests(self):
        yield SeleniumRequest(
            url="https://duckduckgo.com",
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):
        # img = response.meta['screenshot']

        # with open('screenshot.png', 'wb') as f:
        #     f.write(img)

        driver = response.meta['driver']
        search = driver.find_element_by_id('search_form_input_homepage')
        search.send_keys("Hello World")
        search.send_keys(Keys.ENTER)
        driver.implicitly_wait(6)
        driver.save_screenshot("1.png")
        html = driver.page_source
        response_obj = Selector(text= html)
        driver.save_screenshot('afterr.png')
        links = response_obj.xpath("//div[@class='result__body links_main links_deep']")
        for link in links:
            yield {
                'Url': link.xpath(".//h2/a[1]/@href").get() 
              }