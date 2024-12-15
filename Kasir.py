print("===Struk Kasir===")
print('')
print('Jawab tanpa huruf kapital!')

print('Menu:')
print('Minuman:')
print('1.Es teh -- 15K')
print('2.Kopi -- 50k')
print('===================')
print('Makanan:')
print('1.Burger -- 145k')
print('2.Ikan Arapaima -- 500k')
print("")
nama_= input ('masukan nama:')
print('____________________')
print ('tunai/kartu')
pembayaran_= (input ('pembayaran mengunakan apa:' ))
print('________________________________________')
banyak_teh = int(input('Masukan banyak teh:'))
banyak_kopi = int(input('Masukan banyak kopi:'))
banyak_burger = int(input('Masukan banyak burger:'))
banyak_ikan = int(input('Masukan banyak ikan:'))

total_=int((banyak_ikan*500000+banyak_teh*15000+banyak_kopi*50000+banyak_burger*145000)*110/100)
print ("")
print ('atas nama :',nama_)
print('____________________')
print('Es teh           :', banyak_teh,             '|harga      :', banyak_teh*15000)
print('Kopi             :', banyak_kopi,            '|harga      :', banyak_kopi*50000)
print('Burger           :', banyak_burger,          '|harga      :', banyak_burger*145000)
print('Ikan Arapaima    :', banyak_ikan,            '|harga      :', banyak_ikan*500000)
print('total:', total_)
print('Tip: 10%')
print ('')

if pembayaran_ == 'tunai':
    print ('')
    pembayaran_2 = int(input('Masukan jumlah pembayaran:'))
    if pembayaran_2 >= total_ :
        kembalian = pembayaran_2 - total_
        print(kembalian)

        print ('jawaban: iya / tidak ')
        tambahan_ = input('Apakah mau menambah kue:')
        if tambahan_ == 'iya' and kembalian > 0:
            print ('Ingin ukuran yang mana?')
            kecil = 50000
            sedang = 500000
            besar = 5000000
            print ('Kecil   harga:50K')
            print ('Sedang  harga:500K')
            print ('Besar   harga:5JT')
            print('------------------')
            ukuran_kue = input('masukan ukuran kue:')
            if ukuran_kue == 'kecil':
                print ('Oke kita sudah terima')
                print('Terima kasih telah datang di Restoran Suka maju')
                if kembalian < kecil:
                    print('Uang anda kurang! anda harus menambahkan:',kecil - kembalian)
            if ukuran_kue == 'sedang ':
                print('Oke kita sudah terima')
                print('Terima kasih telah datang di Restoran Suka maju')
                print('Uang anda kurang! anda harus menambahkan:', sedang - kembalian)
            if ukuran_kue == 'besar':
                print('Oke kita sudah terima')
                print('Terima kasih telah datang di Restoran Suka maju')
                print('Uang anda kurang! anda harus menambahkan:', besar - kembalian)
        else:
            print('Terima kasih telah datang di Restoran Suka maju')
    else:
        print ('Uang tidak cukup! anda kurang',pembayaran_2 - total_)
else:
    print ('iya/tidak')
    bonus = input('apakah anda mau bonus:')
    if bonus == 'mau':
        print ('oke bonus nya kue')
        print('terima kasih telah datang di restoran suka maju')
    else:
        print ('terima kasih telah datang di restoran suka maju')
#yang ken udah
#nama_= input ('masukan nama:')
#pembayaran_= (input ('pembayaran mengunakan apa:' ))
#print ("")
#print ('atas nama :',nama_)
#print('____________________')
#print('Es teh           :', banyak_teh,             '|harga      :', banyak_teh*15000)
#print('Kopi             :', banyak_kopi,            '|harga      :', banyak_kopi*50000)
#print('Burger           :', banyak_burger,          '|harga      :', banyak_burger*145000)
#print('Ikan Arapaima    :', banyak_ikan,            '|harga      :', banyak_ikan*500000)
#print('total:', total_)
#print ('')
#if pembayaran_ == 'tunai':
    #print ('')
    #pembayaran_2 = int(input('masukan jumlah pembayaran:'))
    #if pembayaran_2 >= total_ :
        #print('kembalian:', pembayaran_2 - total_)
        #print ('iya boleh /tidak maksih')
        #tambahan_ = input('apakah mau menambah kue:')
        #if tambahan_ == 'iya boleh':
            #print ('kamu harus menambah uwang')
            #print ('iya / tidakusa')
            #tambah_uwang = input ('mau menambah uwang?:')
            #print ('mau ukuran berapa')
            #print ('kecil   harga:50000')
            #print ('sedang  harga:500000')
            #print ('besar   harga:5000000')
            #ukuran_kue = input('masukan ukuran kue:')
            #if ukuran_kue == 'kecil':
                #print ('oke kita sudah terima')
                #print('terima kasih telah datang di restoran suka maju')
            #if ukuran_kue == 'sedang ':
                #print('oke kita sudah terima')
                #print('terima kasih telah datang di restoran suka maju')
            #if ukuran_kue == 'besar':
                #print('oke kita sudah terima')
                #print('terima kasih telah datang di restoran suka maju')
        #else:
            #print('terima kasih telah datang di restoran suka maju')
    #else:
        #print ('unag tidak cukup')
#else:
    #print ('mau/tidak')
    #bonus= input('apakah anda mau bonus:')
                #if bonus == 'mau':
                    #print ('oke bonus nya kue')
                    #print('terima kasih telah datang di restoran suka maju')
               # else:
                     #print ('terima kasih telah datang di restoran suka maju')