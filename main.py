import phonenumbers
from test import numbers  # <-- plural variable import
from phonenumbers import geocoder, carrier

for number in numbers:
    try:
        # Location (CH for Switzerland)
        ch_number = phonenumbers.parse(number, "CH")
        location = geocoder.description_for_number(ch_number, "en")

        # Carrier (RO for Romania)
        service_number = phonenumbers.parse(number, "RO")
        carrier_name = carrier.name_for_number(service_number, "en")

        print(f"Number: {number}")
        print(f"Location: {location}")
        print(f"Carrier: {carrier_name}")
        print("_" * 40)
    except phonenumbers.NumberParseException:
        print(f"Invalid number: {number}")
        print("_" * 40)
