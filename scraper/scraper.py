from bs4 import BeautifulSoup
import json
import requests

user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }

hn_url = 'https://news.ycombinator.com/'

# creates a json file of filtered items
def main():

    download_page_src(hn_url)

    with open('page_src.html', encoding='utf-8') as page_src:
        source = page_src.read()

    soup = BeautifulSoup(source, 'html.parser')

    submissions = get_submissions(soup)

    with open('submissions.json', 'w') as f:
        json.dump(submissions, f, indent=4)

# returns a submissions array, which contains parsed titles
def get_submissions(soup):
    submissions = []

    page_result = soup.select('.itemlist')

    #with open("Output.txt", "w") as text_file:
    #    print("Page Result: {}".format(page_result), file=text_file)

    for result in page_result:
        title = result.select('.title a')[0].text.strip()
        submissions.append({
            'title': title
        })

    return submissions

# downloads url and saves it as page_src.html
def download_page_src(url):
    print(url)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    with open('page_src.html', 'w', encoding='utf-8') as saved_page:
        saved_page.write(soup.prettify(encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    main()
