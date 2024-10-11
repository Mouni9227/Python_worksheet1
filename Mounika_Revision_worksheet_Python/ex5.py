#wavelength and corresponding VIBGYOR color
def get_color(w):
    if w<380 or w>750:
        return "Other than VIBGYOR color range,Please enter a wavelength in the range of 380nm to 750nm"
    elif w<450:
        return "Violet"
    elif w<495:
        return "Blue"
    elif w<570:
        return "Green"
    elif w<590:
        return "Yellow"
    elif w<620:
        return "Orange"
    else:
        return "Red"

def main():
    w=int(input("Enter a wavelength in nm: "))
    print(f'The wavelength {w}nm comes under',get_color(w),'color of the EM spectrum ')

if __name__ =="__main__":
    main()