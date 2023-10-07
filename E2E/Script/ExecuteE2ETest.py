import e2e_test_script

e2e_test_script.login("testuser01!@#", "testpassword")
e2e_test_script.add_item_to_cart("Laptops", "MacBook air")
e2e_test_script.place_order("Testuser", "UK", "London", "12345", "Aug", "2023")
