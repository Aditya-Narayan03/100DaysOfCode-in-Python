import csv

#opening the original csv file in read mode
with open('username.csv', 'r') as csv_file:

    #reading the csv file
    csv_reader = csv.reader(csv_file)


    #opening the new csv file in write mode
    with open('new_username.csv', 'w') as new_file:

        #writing the file and setting the delimiter to be ';'
        csv_writer = csv.writer(new_file, delimiter=';')
        
        print("Original Data : \n")

        #this loop will read every single line
        for line in csv_reader: 
            print(line)

            #when the line is read this will replace ',' with ';'
            # and write it to the new file specified
            csv_writer.writerow(line) 


    #again opening the new saved file in read mode
    with open('new_username.csv', 'r') as file_reader:

        #reading the new file
        new_username_reader = csv.reader(file_reader)

        print("\n\nReplaced data :\n")

        #this will iterate and read every line
        for line in new_username_reader:

            #after reading the line we will print it
            print(line)

        print("\n")

