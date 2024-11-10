# TODO Найдите количество книг, которое можно разместить на дискете

Vol_MB = 1.44
Pages = 100
Lines = 50
Symbol = 25
Storage_spase_Bytes = 4
MB = 1024
KB = 1024

Vol_Bytes = Vol_MB * MB * KB

Vol_Books = Pages * Symbol * Lines * Storage_spase_Bytes

Books = Vol_Bytes / Vol_Books

Books = round(Books)

print("Количество книг, помещающихся на дискету:", Books)
