from DLalgorithms import gradienrdescent_basic as gd

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main(slc_num):
    # Check if the number is positive or negative
    if slc_num < 0:
        gus_nm = gd.prd_postv(slc_num)
        rst = gd.check_prd(gus_nm, slc_num)
        return rst

    else:
        print("Please enter a positive number")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    usr_num = eval(input("Select a positive number:"))
    result = main(usr_num)
    print(result)
