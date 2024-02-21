def intValidation(data):
    try:
        int(data)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    print("==============================================================")
    print("= Jumlah input bisa lebih dari satu, dipisahkan dengan koma. =")
    print("==============================================================")
    print("")
    user_input = input("Masukan input berupa angka: ")
    inputs_list = user_input.split(',')
    total_sum = 0
    output = ''
    for inpt in inputs_list:
        isInteger = intValidation(inpt)
        if(isInteger != True):
            output = "Salah satu inputan bukan berupa integer."
            break
        else:
            total_sum += int(inpt)
            output = "Total dari penjumlahan data input adalah " + str(total_sum)
    print()
    print("output : ", output)
    print("==============================================================")
    