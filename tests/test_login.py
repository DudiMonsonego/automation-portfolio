import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_full_purchase_flow(page):
    # 1. Login
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # 2. Inventory - Add to cart
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    
    # Assert - וודא שהמוצר נוסף לעגלה
    assert inventory.get_cart_count() == "1"
    
    # 3. Move to cart
    inventory.go_to_cart()
    assert "/wrong-page.html" in page.url

@pytest.mark.parametrize("item_name", ["sauce-labs-backpack", "sauce-labs-bike-light"])
def test_add_multiple_items(page, login_page, inventory_page, item_name):
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # לוקטור דינמי לפי שם המוצר
    page.click(f"[data-test='add-to-cart-{item_name}']")
    assert inventory_page.get_cart_count() == "1"