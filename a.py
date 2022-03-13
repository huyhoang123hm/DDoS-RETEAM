import requests
check='5'
if check=='5':
    a=''
    a=a+requests.get(url='https://gist.githubusercontent.com/Azuures/1e0cb7a1097c720b4ed2aa63acd82179/raw/97d2d6a11873ffa8ca763763f7a5dd4035bcf95f/fwefnwex').text.strip()+'\n'
    a=a+requests.get(url='https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text.strip()+'\n'
    file=open('socks4.txt','w')
    file.write(a)
    file.close()
    file=open('socks4.txt')
    a=file.readlines()
    file.close()
    file=open('live.txt','w')
    file.close()
    file=open('socks4.txt','w')
    for i in a:
      if i.strip()!='':
        file.write(i)
    file.close()

else:
    a=''
    a=a+requests.get(url='https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all').text.strip()+'\n'
    a=a+requests.get(url='https://www.proxy-list.download/api/v1/get?type=socks4').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt').text.strip()+'\n'
    file=open('socks4.txt','w')
    file.write(a)
    file.close()
    file=open('socks4.txt')
    a=file.readlines()
    file.close()
    file=open('socks4.txt','w')
    for i in a:
      if i.strip()!='':
        file.write(i)
    file.close()
