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


def test_product_page_has_size_selector_and_add_to_cart_button(page):
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=30000)

    first_card = page.locator(".js-product.t-store__card").first
    product_link = first_card.locator("a[href*='/tproduct/']").first

    product_link.click()

    page.wait_for_url("**/tproduct/**", timeout=10000)

    product_options = page.locator(".js-product-controls-wrapper").first

    expect(product_options.locator(".js-product-edition-option-name")).to_contain_text("Размер")

    expect(product_options.locator("label:has(input[value='S'])")).to_be_visible()
    expect(product_options.locator("label:has(input[value='M'])")).to_be_visible()
    expect(product_options.locator("label:has(input[value='L'])")).to_be_visible()
    expect(product_options.locator("label:has(input[value='XL'])")).to_be_visible()

    add_to_cart_button = page.get_by_text("ДОБАВИТЬ В КОРЗИНУ", exact=True).first
    expect(add_to_cart_button).to_be_visible()


def test_add_product_to_cart_shows_success_message(page):
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=30000)

    first_card = page.locator(".js-product.t-store__card").first
    product_name = first_card.locator(".js-product-name").inner_text().strip()
    product_link = first_card.locator("a[href*='/tproduct/']").first

    product_link.click()

    page.wait_for_url("**/tproduct/**", timeout=10000)

    add_to_cart_button = page.get_by_text("ДОБАВИТЬ В КОРЗИНУ", exact=True).first
    expect(add_to_cart_button).to_be_visible(timeout=10000)

    add_to_cart_button.click()

    success_message = page.locator(".t706__bubble-text").first

    expect(success_message).to_contain_text(
        f"{product_name} добавлено в корзину",
        timeout=10000
    )