import csv #needed to parse CSV file
import datetime #needed to convert begin and end dates to epoch time for comparison with timestamps

# create date objects for begin and end date, along with lists to store rows from the file and words from each row
begin_date = datetime.date(2014,6,22)
end_date = datetime.date(2014,7,22)
rows = []
words = []

# open CSV file and read each row except header
csvfile = open('sample_data.csv')
readCSV = csv.reader(csvfile)
readCSV.next() #skips header row in CSV file

# for each row, convert created_at from epoch date to date object and store if date is within desired range
for row in readCSV:
    created_at = row[1]
    created_at_float = float(created_at)
    created_at_date = datetime.date.fromtimestamp(created_at_float)
    if created_at_date >= begin_date and created_at_date < end_date:
        rows.append(row)

# check my work by writing each word to a list and printing to get the phrase
for record in rows:
    date = datetime.date.fromtimestamp(float(record[1]))
    word = record[8]
    words.append(word)
print(words)    

    