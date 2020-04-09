import sys

enc_key = 'SiuHungIsAGoodBearBecauseHeIsVeryGood'

def dec_lf2_data(enc_file_path, dec_file_path):
    enc_file = open(enc_file_path,'rb').read()
    dec_file = open(dec_file_path,'a')

    index=12
    for i in range(123,len(enc_file)):
        dig =  enc_file[i]-ord( enc_key[index] )
        if dig < 0: dig += 0x100
        
        dec_file.write(chr(dig))
        index +=1
        if index == len(enc_key): index = 0

def enc_lf2_data(enc_file_path, dec_file_path):
    enc_file_og = open(enc_file_path,'rb').read()
    enc_file_output = open(enc_file_path + '.2','ab')
    dec_file = open(dec_file_path, 'rb').read()
    for i in range(0,123):
        arr = []
        arr.append(enc_file_og[i])
        enc_file_output.write(bytes(arr))

    index = 12
    for i in range(0, len(dec_file)):
        dig =  dec_file[i] + ord(enc_key[index])
        
        if dig < 0: dig += 0x100

        arr = []
        arr.append(dig)
        
        enc_file_output.write( bytes(arr))
        index +=1
        if index == len(enc_key): index = 0

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("supply the encryption and decryption file path using command line.")
        exit()

    print("\n\n********lf2 moder********")
    print("\nUSAGE: decrypt "".dat"" file modify it, encrypt it and replace with the original one.")
    op = int(input("\nenter 1 for decryption, 0 for encryption \n"))

    if op == 0: enc_lf2_data(sys.argv[1], sys.argv[2])
    elif op == 1: dec_lf2_data(sys.argv[1], sys.argv[2])
    else:
        print("Wrong action.")
        exit()

    print("\n********done.********\n")
    print("replace the original file with moded one.(It is recommended to backup the original one)\n")
    
