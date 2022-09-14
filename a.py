import requests
check='4'
if check=='5':
    a=''
    a=a+requests.get(url='https://api.good-proxies.ru/get.php?type%5Bsocks5&key=3269305ce8094af10e5933fe67db8529').text.strip()+'\n'
    a=a+requests.get(url='https://gist.githubusercontent.com/Azuures/1e0cb7a1097c720b4ed2aa63acd82179/raw/97d2d6a11873ffa8ca763763f7a5dd4035bcf95f/fwefnwex').text.strip()+'\n'
    a=a+requests.get(url='https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/RX4096/proxy-list/main/online/socks5.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt').text.strip()+'\n'
    a=a+requests.get(url='https://www.proxy-list.download/api/v1/get?type=socks5').text.strip()+'\n'
    a=a+requests.get(url='https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=5000&country=all&ssl=all&anonymity=all').text.strip()+'\n'
    a=a+requests.get(url='https://openproxylist.xyz/socks5.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt').text.strip()+'\n'
    a=a+requests.get(url='http://pubproxy.com/api/proxy?limit=10&format=txt&type=socks5').text.strip()+'\n'
    a=a+requests.get(url='http://www.proxylists.net/socks5.txt').text.strip()+'\n'

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

else:
    a=''
    a=a+requests.get(url='https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all').text.strip()+'\n'
    a=a+requests.get(url='https://www.proxy-list.download/api/v1/get?type=socks4').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/RX4096/proxy-list/main/online/socks4.txt').text.strip()+'\n'
    a=a+requests.get(url='https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=5000&country=all&ssl=all&anonymity=all').text.strip()+'\n'
    a=a+requests.get(url='https://openproxylist.xyz/socks4.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt').text.strip()+'\n'
    a=a+requests.get(url='http://pubproxy.com/api/proxy?limit=10&format=txt&type=socks4').text.strip()+'\n'
    a=a+requests.get(url='http://www.proxylists.net/socks4.txt').text.strip()+'\n'
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
