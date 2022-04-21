from time import sleep
from login import cloudlogin as login
from locate import cloudlocate as locate
from search import cloudsearch as search
from jobs import cloudjobs as jobs

iplist = [
]
idlist = [
]
namelist = [
]


def mycode(page):
    login.loginPrd(page)
    locate.locateEcs(page)
    for id, name in zip(idlist, namelist):
        jobs.renameEcs(page, id, name, 1)