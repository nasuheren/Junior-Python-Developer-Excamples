#  Toplam Hesaplama

# a = int(input("1."))
# b = int(input("2."))

# print(a + b)




#  Tek mi Çift mi?

# a = int(input("deger"))

# if a % 2 == 0:
#     print("Cift")
# else:
#     print("TEK")




# Faktöriyel Hesaplama

# a = int(input("deger"))
# b = 1

# for i in range(a+1):
#     if i != 0:
#         b = i * b

# print(b)




#  Fibonacci Serisi

# a = int(input("deger"))

# b = 0
# x = 1

# liste = []
# for i in range(a):
#     liste.append(b)
#     x, b = b, x + b

# print(liste)




#  Palindrom Kontrolü

# def is_palindrome(word):
#     word = word.lower()  # Büyük/küçük harf duyarlılığını kaldır
#     return word == word[::-1]  # Kelimenin tersini al ve karşılaştır

# # Kullanıcıdan giriş al
# word = input("Bir kelime girin: ")
# if is_palindrome(word):
#     print(f"'{word}' bir palindromdur.")
# else:
#     print(f"'{word}' bir palindrom değildir.")




# En Büyük Sayıyı Bulma

# def find_max(a, b, c):
#     max_num = a  # Start with 'a' as the maximum number
#     if b > max_num:  
#         max_num = b  # Update if 'b' is greater
#     if c > max_num:  
#         max_num = c  # Update if 'c' is greater
#     return max_num  # Return the largest number

# # Get input from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# # Find and print the maximum number
# max_number = find_max(num1, num2, num3)
# print(f"The largest number is: {max_number}")




# Liste İçinde En Küçük Sayıyı Bulma

# sayilar = [10, 5, 8, 3, 12]

# min = sayilar[0]
# for i in range(len(sayilar)):
#     if min > sayilar[i]:
#         min = sayilar[i]

# print("min: ", min)




# Ters Çevirme

# metin = input("metin girin:")

# ters_metin = metin[::-1]
# print(ters_metin)




# Liste Elemanlarını Çarpma

# sayilar = [2, 3, 4, 5]

# a = 1
# for i in sayilar:
#     a = a * i

# print(a)




# Sayı Tahmin Oyunu

# import random

# a = random.randint(1,10)

# while True:
#     sayi = int(input("sayi gir:"))
#     if a == sayi:
#         print("dogru")
#         break
#     elif a < sayi:
#         print("kucuk gir")
#     elif a > sayi:
#         print("buyuk gir")