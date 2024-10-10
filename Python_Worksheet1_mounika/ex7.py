from importlib.resources import read_text
#getting individual digits
def ind_digits(n):
    digit = []
    for d in n:
     digit.append(int(d))
    return digit

def main():
  n =input('Enter a number:')
  print(f'The individual digits of {n} are :', ind_digits(n))

if __name__ == "__main__":
  main()
