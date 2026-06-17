from playwright.sync_api import expect

BASE_URL = "https://opensymbols.shop/"


def test_open_first_product_card(page):
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=30000)

    first_card = page.locator(".js-product.t-store__card").first
    product_name = first_card.locator(".js-product-name").inner_text().strip()
    product_link = first_card.locator("a[href*='/tproduct/']").first

    product_link.click()

    page.wait_for_url("**/tproduct/**", timeout=10000)

    expect(page.locator("body")).to_contain_text(product_name, timeout=10000)