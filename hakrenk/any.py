if __name__ == '__main__':
    s = input()
    print (any(j.isalnum()  for j in s))
    print (any(j.isalpha() for j in s))
    print (any(j.isdigit() for j in s))
    print (any(j.islower() for j in s))
    print (any(j.isupper() for j in s))
