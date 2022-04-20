from asyncio.windows_events import NULL


def searchEcsByIp(page, ipAddress: str):
    page.wait_for_load_state(state='load')
    page.wait_for_load_state(state='networkidle')
    try:
        page.locator("xpath=//*/div[2]/div/div[2]/div/div[2]/span[1]").click()
        page.locator("text=IP地址").click()
    except:
        NULL
    page.locator("[placeholder=\"输入IP地址模糊查询\"]").fill(ipAddress)
    page.locator("text=搜 索").click()
    if page.locator('text=没有数据').count() != 0:
        return False
    return True
