import pytest

from src.scraping_stocks import (
    get_status_code,
    get_stock_company_name,
    get_stock_company_price,
)


@pytest.mark.webtest
def test_get_status_code():
    url = "https://www.investing.com/equities/nike"
    assert get_status_code(url) == 200


@pytest.mark.parametrize(
    "url, company_name",
    [
        ("https://www.investing.com/equities/nike", "Nike Inc (NKE)"),
        ("https://www.investing.com/equities/coca-cola-co", "Coca-Cola Co (KO)"),
        (
            "https://www.investing.com/equities/microsoft-corp",
            "Microsoft Corporation (MSFT)",
        ),
    ],
)
def test_get_stock_company_name(url, company_name):
    company = get_stock_company_name(url)
    assert company == company_name


@pytest.mark.parametrize(
    "url, d_type",
    [
        ("https://www.investing.com/equities/nike", float),
        ("https://www.investing.com/equities/coca-cola-co", float),
        ("https://www.investing.com/equities/microsoft-corp", float),
    ],
)
def test_get_stock_company_price(url, d_type):
    price = get_stock_company_price(url)
    assert type(price) == d_type


if __name__ == "__main__":
    url = "https://www.investing.com/equities/nike"
    print("try the functions on the website: ")
    status_code = get_status_code(url)
    print(f"status code of the website: {status_code}")
    company_name = get_stock_company_name(url)
    print(f"Name of the stock: {company_name}")
