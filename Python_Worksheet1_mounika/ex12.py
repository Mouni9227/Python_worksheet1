def highest_frequency(s):
    freq={}
    for letter in s:
        if letter in freq:
            freq[letter]=freq[letter]+1
        else:
            freq[letter]=1
    result= max(freq, key = freq.get)
    return result

def main():
   s=input("Enter a string: ")
   s="".join(s.split())
   print(f'The highest frequency of character in the string "{s}" is', highest_frequency(s))

if __name__ =="__main__":
   main()

