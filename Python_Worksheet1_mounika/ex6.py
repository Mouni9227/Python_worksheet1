#6, prime number check
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True

def main():
  n=int(input('Enter a number:'))
  if n==1:
      print("It is neither a prime or a composite number")
  elif n<=0:
      print("Please enter a non-zero or non-negative number")
  else:
      print(f'{n} is a prime number :' , is_prime(n))

if __name__ =="__main__":
     main()
