#1
import re

text = "Please contact us at support@example.com or sales@example.org for more information."
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
print(emails)

#2

text = "You can reach us at +7 (912) 345-67-89 or +7 (901) 234-56-78 during business hours."
phone_numbers = re.findall(r'\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}', text)
print(phone_numbers)

#3
text = "Join the discussion on #python and share your thoughts on #regex. Don't forget to tag #coding!"
hashtags = re.findall(r'#\w+', text)
print(hashtags)

#4

text = "Visit our website at https://example.com or check out http://test.org for more details."
urls = re.findall(r'https?://[^\s]+', text)
print(urls)

#5

text = "The total cost is 150 dollars, but you can get a discount of 25 if you buy 3 items."
numbers = re.findall(r'\d+', text)
print(numbers)
#6

text = "The project deadline is 15/10/2023, and the final review will be on 20/12/2023."
dates = re.findall(r'(?:[0-2][0-9]|3[0-1])/(?:0[0-9]|1[0-2])/[0-9]{4}', text)
print(dates)
#7

text = "Python is a popular programming language. Learn Regex to improve your Skills."
capital_words = re.findall(r'[A-Z][a-z]*\b', text)
print(capital_words)
#8

text = "The server IPs are 192.168.1.1, 10.0.0.1, and 8.8.8.8. Avoid using invalid IPs like 999.999.999.999."
ip_addresses = re.findall(r'(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)', text)
print(ip_addresses)
#9

text = "The meeting starts at 14:30 and ends at 16:45. Please arrive by 14:15."
times = re.findall(r'\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9]\b', text)
print(times)

#10

text = "She is singing and dancing while cooking dinner. The evening is full of fun activities."
ing_words = re.findall(r'\w+ing\b', text)
print(ing_words)

#5.2

def decode_val(bits):
    # Декодируем биты, выбирая наиболее часто встречающийся бит в каждом триплете
    return ''.join('1' if triplet.count('1') > triplet.count('0') else '0'
                   for triplet in (bits[i:i+3] for i in range(0, len(bits), 3))
                   if len(triplet) == 3)

def binary_to_char(binary_str):
    # Преобразуем двоичную строку в символ
    return chr(int(binary_str, 2))

def decode_message(encoded_message):
    decoded_message = ""
    for number in encoded_message:
        # Преобразуем число в 24-битную двоичную строку
        binary_str = bin(number)[2:].zfill(24)
        # Декодируем биты
        decoded_bits = decode_val(binary_str)
        # Разбиваем декодированные биты на байты и преобразуем в символы
        decoded_message += ''.join(binary_to_char(decoded_bits[i:i+8])
                          for i in range(0, len(decoded_bits), 8) if len(decoded_bits[i:i+8]) == 8)
    return decoded_message

# Закодированное сообщение
encoded_message = [
    815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912,
    2067455, 2093116, 1044928, 2064407, 6262776, 2027968, 4423680, 2068231,
    2068474, 1999352, 1019903, 2093113, 2068439, 2064455, 1831360, 1936903,
    2067967, 2068456
]

# Декодируем сообщение
decoded_message = decode_message(encoded_message)
print(decoded_message)
