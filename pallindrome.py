def is_pallindrome(s):
    s=s.lower()
    return s==s[::-1]
if __name__=="__main__":
    input=input("enter string:")
    if is_pallindrome(s):
        print("string is pallindrome")
    else:
        print("string is not pallindrome")