from asyncio.windows_events import NULL
import os
from time import sleep
from playwright.sync_api import Playwright, expect, sync_playwright
from mycode import mycode


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="msedge", headless=False)
    context = browser.new_context(ignore_https_errors=True,no_viewport=True)
    page = context.new_page()
    mycode(page)
    os.system("pause")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
