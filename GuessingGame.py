import random
level = ''

while level == '':
        level = input('''Choose you level: 
        E for easy
        M for medium
        H for Hard
        >''').lower()
        if level == 'h':
            guess_count = 0
            guess_limit = 3
            print(f'You have {guess_limit} guesses available')


            while guess_count < guess_limit:
                guess = int(input('Guess a number between 1 - 50: '))
                secret_number = random.randint(1,50)

                if guess!= secret_number:
                    print('Guess not correct, Please try again')
                    guess_count += 1
                    print(f'You have {guess_limit-guess_count} guesses left')

                else:
                     print('You won')
                     break

            else:
                 print(f'You lost! The correct guess was {secret_number}')
                 break

        if level == 'm':
                guess_count = 0
                guess_limit = 4
                print(f'You have {guess_limit} guesses available')


                while guess_count < guess_limit:
                    guess = int(input('Guess a number between 1 - 20:  '))
                    secret_number = random.randint(1, 20)

                    if guess!= secret_number:
                        print('Guess not correct, Please try again')
                        guess_count += 1
                        print(f'You have {guess_limit-guess_count} guesses left')

                    else:
                         print('You won')
                         break

                else:
                     print(f'You lost! The correct guess was {secret_number}')
                     break

        if level == 'e':
            guess_count = 0
            guess_limit = 6
            print(f'You have {guess_limit} guesses available')

            while guess_count < guess_limit:
                guess = int(input('Guess a number between 1 - 10: '))
                secret_number = random.randint(1, 10)

                if guess != secret_number:
                    print('Guess not correct, Please try again')
                    guess_count += 1
                    print(f'You have {guess_limit - guess_count} guesses left')

                else:
                    print('You won')
                    break

            else:
                print(f'You lost! The correct guess was {secret_number}')
                break


else:
    print('Invalid input, please try again')


