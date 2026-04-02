hari = int(input("Masukan jumlah hari: "))

tahun = hari // 365
sisa_hari = hari % 365

bulan = sisa_hari // 30
sisahari = sisa_hari % 30

print("Tahun :", tahun)
print("Bulan :", bulan)
print("Hari  :", sisahari)