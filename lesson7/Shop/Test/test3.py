from lesson7.Shop.Page.shopmain import ShopMainPage
from lesson7.Shop.Page.container import ShopContainer

def test_shop(chrome_browser):
    expected_total = "58.29"

    shopmain = ShopMainPage(chrome_browser)
    shopmain.registration_fields()
    shopmain.buy_issue()
    shopmain.click_issue()
    shopmain.into_container()

    container = ShopContainer(chrome_browser)
    container.checkout()
    container.info()
    container.price()
    assert expected_total in container.price()
    print(f"Итоговая сумма равна ${container.price()}")