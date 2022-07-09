import asyncio
import pyppeteer as pyp
import time

async def antiAntiCrawler(page):   #为page添加反反爬虫手段
    await page.setUserAgent('Mozilla/5.0 (Windows NT 6.1; \Win64; x64)')
    await page.evaluateOnNewDocument('()=>{Object.defineProperties(navigator,\{webdriver:{get:()=>false}})}')

async def getOjSourceCode(loginUrl):
    account=''
    password=''
    width,heigth=1400,800  #网页宽高
    broswer=await pyp.launch(headless=False, executablePath='D:\chromium\chrome-win\chrome.exe',args=[f'--window-size={width},{heigth}'])
    page=await broswer.newPage()
    await antiAntiCrawler(page)    #添加反反爬虫手段
    await page.setViewport({'width':width,'height':heigth})
    await page.goto(loginUrl)
    element = await page.querySelector('#fm-login-id')  #找到手机号输入框
    await element.type(account)  #输入手机号
    time.sleep(2)  #停顿两秒
    element = await page.querySelector('#fm-login-password')  #找到密码输入框
    await element.type(password)  #输入密码
    time.sleep(2)
    element = await page.querySelector('.fm-button')  #找到登录按钮
    await element.click()  #点击登录
    #TODO 点击登录之后会有滑动验证，手动/自动操作会导致失败
    #TODO 尝试html代码中设置webdrive，但是仍然不行
    # TODO 大部分通道都被淘宝限制了
    await page.waitForSelector('#mx_5 > div.pc-search-filter.J_pc-search-filter > div.bar-group.clearfix.order-bar.clearfix')  #等待标志出现
    element = await page.querySelector('#J_SiteNavBdR > li.J_Menu.menu.my-taobao > div.menu-hd.J_MenuMyTaobao > a')  #找到我的淘宝
    await element.click()
    await page.waitForNavigation()  #等待页面出现
    element = await page.querySelector('#bought')  #找到我买过的宝贝
    await element.click()
    await page.waitForNavigation()
    elements = await page.querySelectorAll(".production-mod__pic___G8alD")  #找到所有订单信息
    page2 = await broswer.newPage()  #新建标签页
    await antiAntiCrawler(page2)
    for element in elements[:5]:
        obj = await element.getProperty("href")  #获取订单网址
        url = await obj.jsonValue()
        await page2.goto(url)
        element = await page2.querySelector("title")
        obj = await element.getProperty("innerText")
        text = await obj.jsonValue()
        print(text)
        print("----------------------")
    await broswer.close()

loginUrl = "https://login.taobao.com/member/login.jhtml?spm=a2e0b.20350158.1997563269.1.a286468apMhevj&f=top&redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3Dtaobao%26clk1%3Ddf42becb4b819028a92dd40818abb781%26upsId%3Ddf42becb4b819028a92dd40818abb781&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_11.87.177.220_6958939_1626761965232%3Bprepvid%3A201_11.87.177.220_6958939_1626761965232&clk1=df42becb4b819028a92dd40818abb781"
loop = asyncio.get_event_loop()
loop.run_until_complete(getOjSourceCode(loginUrl))