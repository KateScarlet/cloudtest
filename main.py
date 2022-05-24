from os import system
from time import sleep
from playwright.sync_api import Playwright, expect, sync_playwright
from jobs import cloudjobs as jobs
from locate import cloudlocate as locate
from login import cloudlogin as login
from search import cloudsearch as search

iplist = [
    
]
idlist = [

]
namelist = [

]


def mycode(page):
    login.loginPrd(page)
    locate.locateEcs(page)
    for ip, name in zip(iplist, namelist):
        jobs.renameEcs(page, ip, name, 0)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="msedge", headless=False)
    context = browser.new_context(ignore_https_errors=True, no_viewport=True)
    page = context.new_page()
    mycode(page)
    system("pause")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
