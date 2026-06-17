from playwright.sync_api import expect

BASE_URL = "https://opensymbols.shop/"


def test_home_page_has_product_cards(page):
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=30000)

    product_cards = page.locator(".js-product.t-store__card")

    expect(product_cards.first).to_be_visible(timeout=10000)
    assert product_cards.count() > 0


def test_first_product_card_has_name_price_and_link(page):
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=30000)

    first_card = page.locator(".js-product.t-store__card").first

    expect(first_card.locator(".js-product-name")).to_be_visible()
    expect(first_card.locator(".js-product-price")).to_be_visible()

    product_link = first_card.locator("a[href*='/tproduct/']").first
    expect(product_link).to_be_visible()