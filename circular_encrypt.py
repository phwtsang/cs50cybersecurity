def main():
    """
    Decode circularly encrypted texts.
    """
    input_str = input('Encrypted text: ')
    for i in range(1,3):
        output_str = ''
        for j in input_str:
            ordj = ord(j)
            if ordj >= 65 and ordj <= 90:
                output_str += chr(ordj+i)
            elif ordj >= 97 and ordj <= 122:
                output_str += chr(ordj+i)
            else:
                output_str += j

        print(i,output_str)


main()