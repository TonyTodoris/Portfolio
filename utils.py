import csv

def write_to_database_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow({data['email'], data['subject'], data['message']})
