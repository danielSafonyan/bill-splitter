import sys
import random


def get_num_friends():
    while True:
        print('Enter the number of friends joining (including you): ')
        num_friends_joining = input()

        try:
            num_friends_joining = int(num_friends_joining)
        except ValueError:
            print("No one is joining for the party")
            sys.exit()

        if num_friends_joining < 1:
            print("No one is joining for the party")
            sys.exit()

        return num_friends_joining


def get_friends_names(num_friends):
    print('Enter the name of every friend (including you), each on a new line:')
    dict_friends_joining = {input(): 0 for _ in range(num_friends)}
    return dict_friends_joining


class BillSplitter:
    def __init__(self):
        self.num_friends = 0
        self.final_bill = 0
        self.friends = dict()
        self.lucky = None

    def take_input(self):
        self.num_friends = get_num_friends()
        print()
        self.friends = get_friends_names(self.num_friends)
        print()
        print("Enter the total bill value:")
        self.final_bill = float(input())
        print()

    def split_the_bill(self):
        split_sum = self.final_bill / self.num_friends
        split_sum = round(split_sum, 2)

        for key in list(self.friends):
            if key == self.lucky:
                continue
            self.friends[key] = split_sum

        print(self.friends)

    def pick_lucky_person(self):
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        answer = input()

        if answer.lower() == "yes":
            self.lucky = random.choice(list(self.friends))
            print(f"\n{self.lucky} is the lucky one!\n")
            self.num_friends -= 1
        else:
            print('No one is going to be lucky')


def main():
    new_bill = BillSplitter()
    new_bill.take_input()
    new_bill.pick_lucky_person()
    new_bill.split_the_bill()


if __name__ == '__main__':
    main()