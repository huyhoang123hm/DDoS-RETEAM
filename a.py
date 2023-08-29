import requests

check = '4'

def fetch_proxy_list(url):
    try:
        response = requests.get(url)
        if response.status_code == 200 and response.text.find('a')==-1:
            return response.text.strip()
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while fetching data from {url}: {str(e)}")
    return ''

if check == '5':
    proxy_urls = [
    'https://api.good-proxies.ru/get.php?type%5Bsocks5&key=3269305ce8094af10e5933fe67db8529',
    'https://gist.githubusercontent.com/Azuures/1e0cb7a1097c720b4ed2aa63acd82179/raw/97d2d6a11873ffa8ca763763f7a5dd4035bcf95f/fwefnwex',
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
    'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
    'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt',
    'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/socks5.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
    'https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
    'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt',
    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt',
    'https://www.proxy-list.download/api/v1/get?type=socks5',
    'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=5000&country=all&ssl=all&anonymity=all',
    'https://openproxylist.xyz/socks5.txt',
    'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt',
    'http://pubproxy.com/api/proxy?limit=10&format=txt&type=socks5',
    ]
    a = '\n'.join([fetch_proxy_list(url) for url in proxy_urls])

    with open('proxy.txt', 'wb') as file:
        file.write(a.encode('utf-8'))
else:
    proxy_urls = [
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all',
    'https://www.proxy-list.download/api/v1/get?type=socks4',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
    'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
    'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt',
    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
    'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/socks4.txt',
    'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=5000&country=all&ssl=all&anonymity=all',
    'https://openproxylist.xyz/socks4.txt',
    'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt',
    'http://pubproxy.com/api/proxy?limit=10&format=txt&type=socks4',
    ]
    
    a = '\n'.join([fetch_proxy_list(url) for url in proxy_urls])

    with open('socks4.txt', 'wb') as file:
        file.write(a.encode('utf-8'))
    
