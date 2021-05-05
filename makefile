all:	docBarGraph.pdf

clean: 
	rm genderzip.txt genderzipfinal.txt zipgendercount.txt women_meansEdit.txt men_meansEdit.txt docBarGraph.pdf

genderzip.txt: npi.gz
	zcat npi.gz | cut -d '|' -f 33,42 > genderzip.txt

genderzipfinal.txt: genderzip.txt zipGenderCount.py~
	python3 zipGenderCount.py~

zipgendercount.txt: genderzipfinal.txt tallyzipgender.py
	python3 tallyzipgender.py

women_meansEdit.txt men_meansEdit.txt: zipgendercount.txt IncomePop.gz incomeGender.py
	python3 incomeGender.py

docBarGraph.pdf: women_meansEdit.txt men_meansEdit.txt makeGraph.py
	python3 makeGraph.py


