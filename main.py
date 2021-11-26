def ekstraksi_data():
    """
    tanggal: 26 November 2021
    waktu: 05: 05:52WIB
    magnitudo: 2.6
    kedalaman :8km
    lokasi: 5.36 LS - 104.51BT
    pusat gempa: Pusat gempa berada di darat 23km BaratLaut Tanggamus
    dirasakan: (Skala MMI): I - II Tanggamus, III Ulu Belu, II Semangka
    :return:
    """
    hasil = dict()
    hasil["tanggal"] = "26 November 2021"
    hasil["waktu"] = "05: 05:52WIB"
    hasil["magnitudo"] = 2.6
    hasil["kedalaman"] = "8km"
    hasil["lokasi"] = {"LS": 5.36, "BT": 104.51}
    hasil["pusat gempa"] = "Pusat gempa berada di darat 23km BaratLaut Tanggamus"
    hasil["dirasakan"] = "(Skala MMI): I - II Tanggamus, III Ulu Belu, II Semangka"
    print(hasil)
    return hasil


def tampilkan_data(result):
    print("Tampilkan data gempa terkini")
    print(f'Tanggal {result["tanggal"]}')
    print(f'Waktu {result["waktu"]}')
    print(f'Magnitudo {result["magnitudo"]}')
    print(f'Kedalaman {result["kedalaman"]}')
    print(f'Lokasi: LS={result["lokasi"]["LS"]}, BT={result["lokasi"]["BT"]}')
    print(f'Pusat gempa {result["pusat gempa"]}')
    print(f'Dirasakan {result["dirasakan"]}')


if __name__ == "__main__":
    print("Aplikasi utama")
    result = ekstraksi_data()
    tampilkan_data(result)
