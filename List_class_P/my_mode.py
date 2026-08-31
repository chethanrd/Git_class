This is write plus read mode math


def my_add(a,b):
    return a+b

lst=[1,2,3,4,5,6,7,8,9]

def is_even(num):
    return True if num%2==0 else False

def my_filter(func,seq):
    out_lst=[]
    for ele in seq:
        if func(ele)==True:
            out_lst.append(ele)
    return out_lst

print(__name__,type(__name__))

def main():
   print(my_filter(is_even,lst))

if __name__=="__main__":
    main()



# when we execute the module directly, then __main__ is set to __main__
# when we import the module directly, then __name__ is set to __module_name__