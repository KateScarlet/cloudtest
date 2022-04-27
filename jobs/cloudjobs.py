from time import sleep
from search import cloudsearch as search


def renameEcs(page, index, name: str, mod: int):  # 重命名ECS名称 ip:mod=0,id:mod=1
    if mod == 0:
        searchResult = search.searchEcsByIp(page, index)
    if mod == 1:
        searchResult = search.searchEcsById(page, index)
    if searchResult == False:
        return
    page.wait_for_load_state(state='load')
    page.wait_for_load_state(state='networkidle')
    page.locator(
        "xpath=//*[@id=\"container\"]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div[2]/div/table/tbody/tr[1]/td/div/div/div/button").click()
    page.wait_for_load_state(state='load')
    page.locator("text=编辑").click()
    page.locator("xpath=//*[@id=\"InstanceName\"]").fill(name)
    page.locator("xpath=//*/span/button[1]").click()


def countRdsCapacity(page, id: str):  # 获取RDS容量
    page.goto(
        f"https://one.console.res.zj.hsip.gov.cn/?productName=rdsnext#/detail/{id}/basicInfo?region=cn-hangzhou-zjybhxq-d01")
    sleep(3)
    capacity = page.locator(
        "xpath=/*/div[1]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[1]/td[1]/span[2]/span[1]").inner_text()
    return capacity
