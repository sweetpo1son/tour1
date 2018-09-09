
def monitor(url,sleeptime):
    import urllib2
    import json
    from time import sleep


    text={
        'ssid':'123',
        'passwd':'456'}

    text = json.dumps(text)


    print(text)

    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
    while True:
        req = urllib2.Request(url=url,data=text,headers=header_dict)
        res = urllib2.urlopen(req)
        html = res.read()
        
        final = json.loads(html)
        '''
        fh = open(str(time.asctime()),"wb")
        fh.write(final)
        fh.close()
        '''
        sleep(sleeptime)