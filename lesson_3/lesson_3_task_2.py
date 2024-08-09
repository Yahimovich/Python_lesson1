from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 13", "+79001234567"),
    Smartphone("Samsung", "Galaxy S22", "+79987654321"),
    Smartphone("Google", "Pixel 6", "+79112223344"),
    Smartphone("OnePlus", "9 Pro", "+79556667788"),
    Smartphone("Xiaomi", "Mi 11", "+79998887766")
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")