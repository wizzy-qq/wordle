# -*- coding: utf-8 -*-
"""wordle.

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ejFqWIUyxFVacgnXmXZI5KsWn7cuJQBT
"""

import random

word_list = ["araba","sesli" , "insan",
            "böcek", "zeytin", "morpa",
            "yüzde", "sınav", "şifre",
            "merak", "narar", "kitap",
            "güven", "yemek", "evrak",
            "şarap", "çanta", "borak",
            "peşin", "duvar", "maske",
            "yavaş", "çimen", "taşla",
            "rüzgar", "çelik","elmas",
            "araba", "tütün","yazım",
            "elmas", "başta","ekmek",
            "akşam", "kalem",
            "bıçak", "şeker", "otlak",
            "çimen", "deniz", "gülüm",
            "çıkış", "kutlu", "yazar",
            "karar", "başla","orman",
            "harfe", "makas","armut",
            "sabah", "yazan", "arkas",
            "yerel", "koyun","kiraz",
            "tahta", "kışla","kılma",
            "karan", "katıl", "altın",
            "yüzey", "taşla",
            "çimen", "nazlı",
            "tekme", "taşla",
            "solma", "bıçak"]

def kelime_sec():
    a = random.choice(word_list)
    return a

def tahmin_al():
    while True:
        tahmin = str(input("Kelime seçilmiştir. Tahmin giriniz: ")).lower()
        if (len(tahmin) == len(tahmin) == 5) and tahmin.isalpha():
            return tahmin
        print("Yanlış kelime. Lütfen 5̳ ̳h̳a̳r̳f̳l̳i̳ kelime giriniz: ")

def cevap(tahmin, dogru_cevap):
    feedback = []
    for i in range(len(tahmin)):

        if tahmin[i] == dogru_cevap[i]:
            feedback.append('🟩')

        elif tahmin[i] in dogru_cevap:
            feedback.append('🟨')

        else:
            feedback.append('⬜')
    return ' ' .join(feedback) #Join bir dizinin elemanlarını belirtilen bir ayraç sembolünü dizi elemanlarının arasına(feedback) koyarak bir string halinde birleştirir.

def play_wordle():
    dogru_cevap = kelime_sec()
    attempts = 6

    print("Wordle'a hoş geldiniz! 5 harfli kelimeyi tahmin etmek için 6 deneme hakkınız var. Sayılar kabul edilmemektedir.")
    print("Yeşil renk (🟩) harfin kelimede bulunduğu ve yerinin de doğru olduğunu gösterir.")
    print("Sarı renk(🟨) harfin kelimede olduğunu ama yerinin yanlış olduğunu belirtir.")
    print("Beyaz renk(⬜) harfin kelimede bulunmadığını belirtir.")
    print("Kelime seçiliyor... Lütfen bekleyiniz.")

    for attempt in range(attempts):
        tahmin = tahmin_al()
        dönüt = cevap(tahmin, dogru_cevap)
        print(f"Cevap: {dönüt}")

        if tahmin == dogru_cevap:
            print(f"Tebrikler! Cevabınız doğruydu. Cevap: {dogru_cevap}")
            break
    else:
        print(f"Üzgünüm lakin doğru cevap buydu: {dogru_cevap}")

if __name__ == "__main__":
    play_wordle()