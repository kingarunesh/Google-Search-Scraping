import requests
from bs4 import BeautifulSoup
import lxml


def search_engine(search):

    #   requests
    END_POINT = f"https://www.google.com/search?q={search}&hl=en&sxsrf=ALiCzsa3tlf3ny9nsA1XRBN4K2Isg5jNdQ%3A1664791497901&source=hp&ei=ybM6Y-_MNO6gseMPnPqr2A8&iflsig=AJiK0e8AAAAAYzrB2WIx8zlwHMSfho2zkSnDmc2heSck&ved=0ahUKEwiv1evO58P6AhVuUGwGHRz9CvsQ4dUDCAc&uact=5&oq={search}&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgjECcyBQgAEIAEMgoIABCABBCHAhAUMgQIABBDMgUILhCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoECC4QQzoLCAAQgAQQsQMQgwE6CAguELEDEIMBOggIABCABBCxAzoICC4QgAQQsQM6CwguEIAEELEDEIMBOggILhCABBDUAlAAWKQGYM8IaABwAHgAgAGbAogBpw2SAQMyLTeYAQCgAQE&sclient=gws-wiz"
    
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    response = requests.get(url=END_POINT, headers=header)
    data = response.text

    #   scraping
    soup = BeautifulSoup(data, "lxml")

    titles_list = soup.select(selector="h3.LC20lb.MBeuO.DKV0Md")
    links_list = soup.select(selector="div.yuRUbf a")
    texts_list = soup.select(selector="div.VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc")

    # print(titles_list)

    titles = []
    for title in titles_list:
        titles.append(title.getText())

    links = []
    for link in links_list:
        links.append(link.get("href"))

    texts = []
    for text in texts_list:
        texts.append(text.getText())

    # print(titles)

    return titles, links, texts
