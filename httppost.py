
def monitor(url,sleeptime):
    from urllib import request,parse
    import json
    from time import sleep


    text={
        'ssid':'123',
        'passwd':'456'}

    text = json.dumps(text).encode(encoding='utf-8')
    #text = parse.urlencode(text).encode(encoding='utf-8')

    print(text)

    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
    while True:
        req = request.Request(url=url,data=text,headers=header_dict)
        res = request.urlopen(req)
        res = res.read()

        html = res.decode(encoding='utf-8')
        final = json.loads(html)
        '''
        fh = open(str(time.asctime()),"wb")
        fh.write(final)
        fh.close()
        '''
        sleep(sleeptime)
