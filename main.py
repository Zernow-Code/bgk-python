import random

batu = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
kertas = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
gunting = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
gambar = [batu, kertas, gunting]

print("Game Suit Sederhana!")
print("Pilih 0 untuk batu, 1 untuk kertas, 2 untuk gunting.")

pilihan_kamu = int(input("Pilihan kamu: "))
print(gambar[pilihan_kamu])

pilihan_komputer = random.randint(0, 2)
print("Pilihan komputer: ")
print(gambar[pilihan_komputer])

if pilihan_kamu >= 3 or pilihan_kamu < 0:
    print("Pilihan idak valid")
elif pilihan_kamu == 0 and pilihan_komputer == 2:
    print("Kamu menang!")
elif pilihan_komputer == 0 and pilihan_kamu == 2:
    print("Kamu kalah")
elif pilihan_komputer > pilihan_kamu:
    print("Kamu kalah")
elif pilihan_kamu > pilihan_komputer:
    print("Kamu menang!")
elif pilihan_komputer == pilihan_kamu:
    print("Seri!")
