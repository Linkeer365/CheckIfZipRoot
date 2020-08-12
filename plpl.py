import os
book_dir="D:\AllDowns\敦煌遺書.uvz"
for each in os.listdir(book_dir):
	if os.path.isdir(each):
		sub=os.listdir(each)[0]
		print("Sub:{}".format(sub))
		os.rename("{}/{}/{}".format(book_dir,each,sub),"{}/{}_2".format(book_dir,sub))
print("done.")