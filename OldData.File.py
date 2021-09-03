# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    f = open("demofile3.txt", "w")
    f.write("897040 AhmedAli 1999\n")
    f.write("901280\n")
    f.write("FarazBaig 2001\n")
    f.write("109991\n")
    f.write("AhmedNaiz 2001\n")
    f.close()

    with open("demofile3.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            print(stripped_line)
    f.close()


    with open("demofile3.txt", "r") as a_file1:
        count = 0
        for line in a_file1:
            for x in line.split():
                print(x)
                if x.isdigit() and len(x) == 6:
                    count += 1;
        print("The Total Count Is")
        print(count)
    f.close()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
