text = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: BIDUPSID=BBFD4B644088C43BD863229C5FE1BC71; PSTM=1606296269; BDRCVFR[kf0al8EeMwC]=mk3SLVN4HKm; BAIDUID=BBFD4B644088C43B8CBAA569122EAAC2:FG=1; BD_HOME=1; H_PS_PSSID=; BAIDUID_BFESS=BBFD4B644088C43B8CBAA569122EAAC2:FG=1; BD_UPN=12314753; BA_HECTOR=20242h0g25a4a00hu81frs8me0q
Host: www.baidu.com
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41
"""

def reqHear_to_py(text):
    hread = {}
    for item in text.strip().split('\n'):
        key, value = item.split(':',1)
        hread[key.strip()] = value.strip()
    return hread

if __name__ == "__main__":
    print(reqHear_to_py(text))