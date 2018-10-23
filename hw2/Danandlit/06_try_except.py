while True:
    user_input = input("Enter an integer. When you are done, type \'done\': ")

    if user_input == 'done':
        print('Thank you for using this program.')
        quit()

    else:
        try:
            user_int = int(user_input)

            if user_int % 2 == 0:
                print('That is an even number!')

        except ValueError:
            print("Not a valid integer. To be done, type \'done\'.")


