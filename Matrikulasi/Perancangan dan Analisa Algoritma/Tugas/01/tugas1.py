def intValidation(data):
    try:
        int(data)
        return True
    except ValueError:
        return False
    
if __name__ == "__main__":
    input_list = []
    input_list += input("Masukan input ke-1: ")
    input_list += input("Masukan input ke-2: ")
    input_list += input("Masukan input ke-3: ")
    input_list += input("Masukan input ke-4: ")
    input_list += input("Masukan input ke-5: ")

    # hitung_total = input_1 + input_2 + input_3 + input_4 + input_5
    total = 0
    output = ""
    for inpt in input_list:
        isInteger = intValidation(inpt)
        if(isInteger != True):
            output = "INPUT HARUS BERUPA ANGKA"
            break
        else:
            total += int(inpt)
            output = "TOTAL : " + str(total)

    print(output)