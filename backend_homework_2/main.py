"""
Empty file
"""
from custom_list import CustomList


if __name__ == '__main__':
    cust_list = CustomList([0, 1, 3, 4, 5, 6, 7])
    cust_list_2 = CustomList([0, 1, 2, 3, 2, 1])
    b = [2, -3, -5] + cust_list_2
    print(b.current_list)
    print(b == cust_list_2)
