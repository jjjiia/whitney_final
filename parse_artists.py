import csv
targetData = []
targetDataFreq = {}

##make an array of the column you want
with open('DataSoFar_04252014.csv', 'rb') as csvfile:    
        spamreader = csv.reader(csvfile)
        
        ages = []
        births = []
        works = []
        years = []
        
        
        for row in spamreader:
            age = row[1]
            birth = str(row[4:6])
            work = str(row[6:8])
            exhibitionYear = row[0]
            
            if age == '2014' or age == '1977':
                print row
            
            ages.append(age)
            births.append(birth)
            works.append(work)
            years.append(exhibitionYear)
            
                

## make a dictionary of frequency of occurence in that column
for i in works:
    targetDataFreq[i] =targetDataFreq.get(i, 0)+1

print targetDataFreq

#for j in  statuses:
    #print j 
   # statusFreq[j] = statusFreq.get(j, 0)+1
#print statusFreq