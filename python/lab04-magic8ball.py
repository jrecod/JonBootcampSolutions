import random
# Magic Eight Ball



print(r"""    __                      __
 .-'  `'.._...-----..._..-'`  '-.
/                                \
|  ,   ,'                '.   ,  |
 \  '-/                    \-'  /
  '._|          _           |_.'
     |    /\   / \    /\    |
     |    \/   | |    \/    |
      \        \"/         /
       '.    =='^'==     .'
         `'------------'`""")
# Welcome Screen
print('Welcome to the Jon\'s Magic 8 Ball!')


def magic8ball():
    # prompt question
    question = input("What is your question?: ")

    # answer pool
    answer = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes – definitely.', 'You may rely on it.',
    'As I see it', 'yes', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy', 'try again.',
    'Ask again later.', 'Better not tell you now.', 'Cannot predict now', 'Concentrate and ask again',
    'Dont count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

    # pick random answer
    random_answer = random.choice(answer)

    # display random answer
    print(random_answer)
    replay()

def replay():
        print ('Would you like to ask another question? [Y/N].')
        reply = input().lower()
        if reply == 'y':
            magic8ball()
        elif reply == 'n':
            print('Thank you for using my program!')
            exit()
        else:
            print('That is not an option, please try again.')
            replay()

magic8ball()