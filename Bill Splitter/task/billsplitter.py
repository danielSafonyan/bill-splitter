def take_input():
    while True:
        print('Enter the number of friends joining (including you): ')
        friends_joining = input()

        try:
            friends_joining = int(friends_joining)
        except ValueError:
            print("No one is joining for the party")
            break

        if friends_joining < 1:
            print("No one is joining for the party")
            break

        list_friends_joining = []

        print('Enter the name of every friend (including you), each on a new line:')
        for i in range(friends_joining):
            list_friends_joining.append(input())

        dict_friends_joining = dict.fromkeys(list_friends_joining, 0)
        print(dict_friends_joining)
        break
take_input()