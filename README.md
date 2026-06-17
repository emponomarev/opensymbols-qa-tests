# Open Symbols QA Tests

Автоматизированные UI-тесты для интернет-магазина Open Symbols Uniform.

## Стек

* Python
* Pytest
* Playwright
* pytest-playwright

## Что проверяется

* открытие главной страницы;
* наличие контента на главной странице;
* отображение карточек товаров в каталоге;
* наличие названия, цены и ссылки у карточки товара;
* переход со страницы каталога на страницу товара;
* отображение размеров товара;
* отображение кнопки добавления в корзину;
* добавление товара в корзину;
* отображение добавленного товара в корзине.

## Установка

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать виртуальное окружение в Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Установить зависимости:

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

## Запуск тестов

```bash
pytest
```

## Структура проекта

```text
tests/
  test_home_page.py
  test_catalog.py
  test_product_page.py
  test_cart.py
```

## Тестируемый сайт

https://opensymbols.shop/
