print(r"""           _.- ~~^^^'~- _ __ .,.- ~ ~ ~  ~  -. _
 ________,'       ::.                       _,-  ~ -.
((      ~_\   -s-  ::                     ,'          ;,
 \\       <.._ .;;;`                     ;           }  `',
  ``======='    _ _- _ (   }             `,          ,'\,  `,
               ((/ _ _,i   ! _ ~ - -- - _ _'_-_,_,,,'    \,  ;
       cfbd       ((((____/            (,(,(, ____>        \,'""")


print('Welcome to my Simple Madlib! ^ that is a platypus!')

#User Choices
noun = input('Enter a noun: ')
name = input('Enter a name: ').capitalize()
windinstrument = input('Enter a wind instrument: ')
stringinstrument = input('Enter a sting intrument: ')


#Filled madlib
message = f'''I've been working on the {noun}
All the live long day
I've been working on the {noun}
Just to pass the time away
Can't you hear the whistle blowing
Rise up so early in the morn
Can't you hear the whistle blowing
{name}, blow your {windinstrument}
{name} won't you blow
{name} won't you blow
{name}, won't you blow your {windinstrument}
{name}, won't you blow,
{name}, won't you blow,
{name}, won't you blow your {windinstrument}
Someone's in the kitchen with {name}
Someone's in the kitchen i know
Someone's in the kitchen with {name}
Strumming on the old {stringinstrument}'''

print(message)