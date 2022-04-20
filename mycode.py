from time import sleep
from login import cloudlogin as login
from locate import cloudlocate as locate
from search import cloudsearch as search
from jobs import cloudjobs as jobs

iplist = [
    "10.147.113.138"]
namelist = [
    "公服区_业务中台_移动支付中心_生产环境_7"]


def mycode(page):
    login.loginGfPrd(page)
    locate.locateEcs(page)
    # for ip, name in zip(iplist, namelist):
    #     jobs.renameEcs(page, ip, name)
    #     sleep(2)
