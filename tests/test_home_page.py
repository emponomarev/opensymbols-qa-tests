BASE_URL = "https://opensymbols.shop/"


def test_home_page_opens(page):
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=30000)

    assert "opensymbols.shop" in page.url


def test_home_page_has_content(page):
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=30000)

    assert page.locator("body").inner_text() != ""