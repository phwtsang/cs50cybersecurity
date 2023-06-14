def main():
    """
    Decode circularly encrypted texts.
    """
    input_str = input('Encrypted text: ')
    for i in range(1,26):
        output_str = ''
        for j in input_str:
            ordj = ord(j)
            #print(ordj)
            if ordj >= 65 and ordj <= 90:
                ordj_new = (ordj-64+i)%26 + 64
                #print(ordj_new)
                output_str += chr(ordj_new)
            elif ordj >= 97 and ordj <= 122:
                ordj_new = (ordj-96+i)%26 + 96
                #print(ordj_new)
                output_str += chr(ordj_new)
            else:
                output_str += j

        print(i,output_str)


main()