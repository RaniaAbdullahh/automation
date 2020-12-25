import re

# input_path="./assets/potential-contacts.txt"
# output_path='emails.txt'
def emails_finder(input_path,output_path):

    with open(input_path,'r') as file:
            file = file.read()
            emails_found =re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", file)

    

    with open(output_path,'w') as result:
        for i in emails_found:
            result.write(f"{str(i)}\n")

    return emails_found        



def phone_numbers_finder(input_path,output_path):
    with open(input_path,'r') as file:
            file = file.read()
            phoneNum_found =re.findall (r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", file)

    with open(output_path,'w') as result:
        for i in phoneNum_found:
            # if len(i)==9 :
            #     i = f"0{i}"
            i = re.sub('[^0-9]+', '', i)
            i = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(i[:-1])) + i[-1]
           
            result.write(f"{str(i)}\n")

    return phoneNum_found        


            











if __name__ == "__main__":
    #print(emails_finder("./assets/potential-contacts.txt",'emails.txt'))
    print(phone_numbers_finder("./assets/potential-contacts.txt",'phone_numbers.txt'))


