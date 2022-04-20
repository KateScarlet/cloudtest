def locateEcs(page):
    page.locator(
        "xpath=//*[@id=\"ascm-topbar-container\"]/div[4]/div[3]/div[1]").click()
    with page.expect_navigation():
        page.locator("text=云服务器 ECS").click()
    return True


def locateRds(page):
    page.locator(
        "xpath=//*[@id=\"ascm-topbar-container\"]/div[4]/div[3]/div[1]").click()
    with page.expect_navigation():
        page.locator("text=云数据库 RDS").click()
    return True


def locateDrds(page):
    page.locator(
        "xpath=//*[@id=\"ascm-topbar-container\"]/div[4]/div[3]/div[1]").click()
    with page.expect_navigation():
        page.locator("text=分布式关系型数据库 DRDS").click()
    return True


def locateOss(page):
    page.locator(
        "xpath=//*[@id=\"ascm-topbar-container\"]/div[4]/div[3]/div[1]").click()
    with page.expect_navigation():
        page.locator("text=对象存储 OSS").click()
    return True


def locateRedis(page):
    page.locator(
        "xpath=//*[@id=\"ascm-topbar-container\"]/div[4]/div[3]/div[1]").click()
    with page.expect_navigation():
        page.locator("text=云数据库 Redis").click()
    return True
