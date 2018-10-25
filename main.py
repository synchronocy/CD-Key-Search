import requests

def scrape(content, web):
    counter = 1
    while True:
        src = requests.get('http://www.bing.com/search?q=%22'+content+'%22+site:'+web+'&first='+str(counter)+'&FORM=PQRE').text
        #<h2><a href=" "
        links = src.split('<h2><a href="')[1:]
        for link in links:
            link = link.split('"')[0]
            if 'pastebin.com' not in link:
                continue
            link = link.replace('https://pastebin.com/','https://pastebin.com/raw/')
            with open(content+'.txt','a') as handle:
                handle.write(link+'\n')
                
            counter = counter + 1

def main():
    content = input('What item do you wish to search? ')
    web = input('On what site? ')
    scrape(content, web)

main()

