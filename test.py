import csv
import datetime
import random
import string

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

with open('source_table_1_2m.csv', 'w',newline='') as f:
    # create the csv writer
    writer = csv.writer(f)

    # Header
    writer.writerow(['TD', 'MRCH_NM', 'MRCH_ST'])

    # write a row to the csv file
    for i in range(2000000):
        writer.writerow([i+1, ''.join(random.choices(string.ascii_uppercase + string.ascii_uppercase, k=3)), random.randint(100,1000)])


with open('source_table_2_2m.csv', 'w',newline='') as f:
    # create the csv writer
    writer = csv.writer(f)

    # Header
    writer.writerow(['TD', 'TXN_AMT', 'TXN_DT'])

    # write a row to the csv file
    for i in range(500000,2500000):
        writer.writerow([i+1, random.randint(100,1000), random_date(datetime.datetime(2018, 1, 1), datetime.datetime(2019, 12, 31)).date().strftime("%m/%d/%Y")])