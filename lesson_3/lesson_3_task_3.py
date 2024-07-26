from address import Address
from mailing import Mailing
to_address = Address("123456", "Москва", "Ленина", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "20", "10")
mailing = Mailing(to_address, from_address, 500.0, "TR123456789")
print(f"Отправление {mailing.track} из {mailing.from_address.postal_code}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.building} - {mailing.from_address.apartment} в {mailing.to_address.postal_code}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.building} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")