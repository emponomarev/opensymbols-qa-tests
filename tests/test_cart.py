from playwright.sync_api import expect

BASE_URL = "https://opensymbols.shop/"


def test_added_product_is_displayed_in_cart(page):
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

    cart_icon = page.locator("a.cartcopy[href='cartcopy_elem']").filter(visible=True).first
    expect(cart_icon).to_be_visible(timeout=10000)
    cart_icon.click()

    cart_window = page.locator(".t706__cartwin-content")

    expect(cart_window).to_be_visible(timeout=10000)
    expect(cart_window.locator(".t706__product-title")).to_contain_text(product_name)
    expect(cart_window).to_contain_text("Размер: S")
    expect(cart_window.locator(".t706__product-quantity")).to_have_text("1")
    expect(cart_window.get_by_text("К оплате", exact=True)).to_be_visible()