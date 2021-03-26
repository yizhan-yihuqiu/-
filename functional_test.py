from selenium import webdriver
#从selenium引入webdriver

brower = webdriver.Firefox()
#启动一个selenium"webdriver"去弹出一个firefox窗口
brower.get('http://localhost:8000')
#用它打开本地网页

assert 'Django' in browser.title
#测试断言，检查在网页Title中有没有“Django”这个词
