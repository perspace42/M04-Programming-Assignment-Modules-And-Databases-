#Import Statement
import csv

#Create Data
books = [
['The Weirdstone of Brisingamen','Alan Garner',1960],
['Perdido Street Station','China Miéville',2000],
['Thud!','Terry Pratchett',2005],
['The Spellman Files','Lisa Lutz',2007],
['Small Gods','Terry Pratchett',1992]
]

#Write Data To CSV file 
with open('book2.csv','wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(books)