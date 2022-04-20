import os
import pyotp
from locate import cloudlocate
import cryptocode


def verifyKey():
    key = input("请输入加密key:")
    verify = "iBHe9LUdJant*gtmg/ILedqqHV2Hdw8hT/w==*XJzPWtufq5D3DvuRb2ZL4g==*OtkTVIUAfyK+1OQEHLUO2Q=="
    if cryptocode.decrypt(verify, key) == "verifyKey":
        print("验证成功")
    else:
        print("验证失败")
        os.system("pause")
        exit()
    return key


key = verifyKey()


cloudTotp = {
    "pre": "Yo+TgPLk8ynYuyxtsy0kCr5s1Zp80uYtgyhGWmaRi9A=*Ucsjb+B8B2avn8hTxkG9eA==*HnPBC2lWEdkZIH348wKHgg==*Cpv5B6VR3rNeaD7YlUiGmg==",
    "prd": "fgwEmc+dmzC6pUNJIWlgoah7t7u1+pvyXs+6g7afKo8=*Qypei3v94DUNgxqtq3w9mw==*BTTMIcZFuEXJtb+sYo6BXg==*04BGS1346VSmC6ejc5G62Q==",
    "gfprd": "6omGaluVOChp2gH6kW9sv9SnZ6mdIV/Nh/VtHdupDiY=*nkp2BTLRWahi5FeDU61HgQ==*jKvly8TQfWyv/HW3IYoNpg==*Iuv7JqVWiWF/PXkwsIZE6w==",
    "gfpre": "zAKqt2j/Kg+EaKNALUaac3UAwLAJu48xr2+ZHuXVZUQ=*3apFdnEpGR+Y4fAO/EerdA==*S/H9M+bH9ap4yl3DzqCbRQ==*lZCc2hDs5K99l5XA4iDdGA=="
}
totpPre = pyotp.TOTP(cryptocode.decrypt(cloudTotp["pre"], key)).now
totpPrd = pyotp.TOTP(cryptocode.decrypt(cloudTotp["prd"], key)).now
totpGfPrd = pyotp.TOTP(cryptocode.decrypt(cloudTotp["gfprd"], key)).now
totpGfPre = pyotp.TOTP(cryptocode.decrypt(cloudTotp["gfpre"], key)).now

cloudUrl = {
    "pre": "https://login.cloud.zj.gov.cn/auth/realms/master/protocol/openid-connect/auth?client_id=ascm_yibao&response_type=code&scope=super&redirect_uri=https://asc.res.zj.hsip.gov.cn/oauth2/authCallback",
    "prd": "https://login.cloud.zj.gov.cn/auth/realms/master/protocol/openid-connect/auth?client_id=ascm_yibao&response_type=code&scope=super&redirect_uri=https://asc.res.zj.hsip.gov.cn/oauth2/authCallback",
    "test": "https://one.console.res.zj.hsip.gov.cn/ascm/login?isOauth=false",
    "gfprd": "https://login.cloud.zj.gov.cn/auth/realms/master/protocol/openid-connect/auth?client_id=ascm_net&response_type=code&scope=super&redirect_uri=https://asc.internet.cloud.zj.gov.cn/oauth2/authCallback",
    "gfpre": "https://login.cloud.zj.gov.cn/auth/realms/master/protocol/openid-connect/auth?client_id=ascm_net&response_type=code&scope=super&redirect_uri=https://asc.internet.cloud.zj.gov.cn/oauth2/authCallback"
}

cloudUser = {
    "pre": ("zhyb_md_pre", "dIi3/oIIyjI=*WovpAsrXsLB2qlwDd/6hAg==*rHftI3/zqalAzOus9j4hZw==*vftHXdPclS65IGzmEEEr/Q=="),
    "prd": ("zhyb_md_prd", "dIi3/oIIyjI=*WovpAsrXsLB2qlwDd/6hAg==*rHftI3/zqalAzOus9j4hZw==*vftHXdPclS65IGzmEEEr/Q=="),
    "test": ("zhyb_md_test", "1FXXps6stYRGSc0=*tWYokOF68ehEwyu+9G7TaQ==*I0jfAi6sYfEF0gaMh4ESbw==*+kF8NVpAyxgFDOqfYOvZMQ=="),
    "gfprd": ("zhyb_ggfw_md_prd", "+g0U+0txjyoDeBMC*hc6lsCGKwjNrGqSrl3Az5Q==*pfUgjxMzP7JvIizVNukbyw==*8nyUirffL08vBlcdBOyXhA=="),
    "gfpre": ("zhyb_ggfw_md_pre", "Yb2hlQQF1S6ho7g=*8YKtMK0cCRz2rXOuixXofw==*qnM5x+phAdRoUsqomF1Mdw==*QUIkdw/TH7tvYXGXWQaFZg==")
}


def loginPre(page):  # 预发环境
    page.goto(cloudUrl["pre"])
    page.locator("[placeholder=\"请输入用户名\"]").fill(cloudUser["pre"][0])
    page.locator("[placeholder=\"请输入密码\"]").fill(
        cryptocode.decrypt(cloudUser["pre"][1], key))
    with page.expect_navigation():
        page.locator("text=登 录").click()
    page.locator("input[name=\"totp\"]").fill(totpPre())
    with page.expect_navigation():
        page.locator("text=登 录").click()
    page.wait_for_load_state(state='load')
    page.wait_for_load_state(state='networkidle')
    return True


def loginPrd(page):  # 生产环境
    page.goto(cloudUrl["prd"])
    page.locator("[placeholder=\"请输入用户名\"]").fill(cloudUser["prd"][0])
    page.locator("[placeholder=\"请输入密码\"]").fill(
        cryptocode.decrypt(cloudUser["prd"][1], key))
    with page.expect_navigation():
        page.locator("text=登 录").click()
    page.locator("input[name=\"totp\"]").fill(totpPrd())
    with page.expect_navigation():
        page.locator("text=登 录").click()
    page.wait_for_load_state(state='load')
    page.wait_for_load_state(state='networkidle')
    return True


def loginTest(page):  # 测试环境
    page.goto(cloudUrl["test"])
    page.locator("[placeholder=\"账户名\"]").fill(cloudUser["test"][0])
    page.locator("[placeholder=\"密码\"]").fill(
        cryptocode.decrypt(cloudUser["test"][1], key))
    with page.expect_navigation():
        page.locator("button:has-text(\"登录\")").click()
    page.wait_for_load_state(state='load')
    page.wait_for_load_state(state='networkidle')
    return True


def loginGfPrd(page):  # 公服生产
    page.goto(cloudUrl["gfprd"])
    page.locator("[placeholder=\"请输入用户名\"]").fill(cloudUser["gfprd"][0])
    page.locator("[placeholder=\"请输入密码\"]").fill(
        cryptocode.decrypt(cloudUser["gfprd"][1], key))
    with page.expect_navigation():
        page.locator("text=登 录").click()
    page.locator("input[name=\"totp\"]").fill(totpGfPrd())
    with page.expect_navigation():
        page.locator("text=登 录").click()
    page.wait_for_load_state(state='load')
    page.wait_for_load_state(state='networkidle')
    return True


def loginGfPre(page):  # 公服预发
    page.goto(cloudUrl["gfpre"])
    page.locator("[placeholder=\"请输入用户名\"]").fill(cloudUser["gfpre"][0])
    page.locator("[placeholder=\"请输入密码\"]").fill(
        cryptocode.decrypt(cloudUser["pgfpre"][1], key))
    with page.expect_navigation():
        page.locator("text=登 录").click()
    page.locator("input[name=\"totp\"]").fill(totpGfPre())
    with page.expect_navigation():
        page.locator("text=登 录").click()
    page.wait_for_load_state(state='load')
    page.wait_for_load_state(state='networkidle')
    return True
