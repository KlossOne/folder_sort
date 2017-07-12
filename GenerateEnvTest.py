import os
import shutil

FOLDER_NAME = 'Download_test'

def delete_Download():
	if(os.path.isdir(FOLDER_NAME) == True):
		shutil.rmtree(FOLDER_NAME)

	return not os.path.isdir(FOLDER_NAME)

def create_file(filename, size):
	f = open(filename,"wb")
	f.seek(1024*size-1)
	f.write("\0")
	f.close()

def create_Download():
	# On cree le dossier
	os.mkdir(FOLDER_NAME)

	# On rentre dans le fossier
	os.chdir(FOLDER_NAME)

	# On cree les fichier
	create_file('film1.avi', 700)
	create_file('musique1.mp3', 4)
	create_file('series1.ep1.avi', 300)
	create_file('series1.ep2.avi', 350)
	create_file('series2.ep1.avi', 300)

if __name__ == '__main__':
	# On supprime le dossier download si existant.
	
	dd = delete_Download()

	if dd != True:
		print "[x] Erreur lors de la suppression du dossier download."
		exit(1)

	print "[*] Dossier Download bien supprime."

	# on cree le dossier

	create_Download()

	print "[*] Dossier et fichier cree."


