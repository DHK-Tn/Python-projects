#Install python barcode Module
from barcode import EAN13
from barcode.writer import ImageWriter

num_barcodes = int(input("How Many Barcodes you Need? "))
for i in range(num_barcodes):
	while 1 :
		id = input("Give 12-Digit numbers for your barcode id: ")
		if len(id)==12:
			break
	my_code = EAN13(id, writer=ImageWriter)
	name_barcode = input("Give the name to save barcodes")
	my_code.save(name_barcode)


