import requests
from bs4 import BeautifulSoup


def get_stock_company_name(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    company = soup.find(
        "h1",
        {
            "class": "text-xl text-left font-bold leading-7 md:text-3xl md:leading-8 mb-2.5 md:mb-2 text-[#232526] rtl:soft-ltr"
        },
    ).text
    return company


def get_stock_company_price(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    price = float(
        soup.find(
            "div",
            {
                "class": "text-5xl font-bold leading-9 md:text-[42px] md:leading-[60px] text-[#232526]"
            },
        ).text
    )
    return price


def get_status_code(url: str):
    page = requests.get(url)
    return page.status_code


if __name__ == "__main__":
    url = "https://www.investing.com/equities/nike"
    print("try the functions on the website: ")
    status_code = get_status_code(url)
    print(f"status code of the website: {status_code}")
    company_name = get_stock_company_name(url)
    print(f"Name of the stock: {company_name}")
