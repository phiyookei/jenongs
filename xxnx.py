def hitung_diskon(total_belanja):
    if total_belanja > 1000000:
        diskon = 0.10  # 10% diskon
    elif total_belanja > 500000:
        diskon = 0.05  # 5% diskon
    else:
        diskon = 0.02  # 2% diskon
    
    jumlah_diskon = total_belanja * diskon
    total_bayar = total_belanja - jumlah_diskon
    
    return total_belanja, diskon, jumlah_diskon, total_bayar

# Contoh penggunaan
total_belanja = float(input("Masukkan total belanja: Rp "))
total_belanja_awal, diskon, jumlah_diskon, total_bayar = hitung_diskon(total_belanja)

print(f"Total belanja awal: Rp {total_belanja_awal:.2f}")
print(f"Diskon: {diskon * 100:.0f}%")
print(f"Jumlah diskon: Rp {jumlah_diskon:.2f}")
print(f"Total yang harus dibayar: Rp {total_bayar:.2f}")