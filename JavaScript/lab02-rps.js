// function rps():

//     player_choice = prompt('Please choose (R) Rock, (P) Paper, or (S) Scissors: ').upper()


//     random_number = random.randint(0,2)


//     // Match numbers with moves
//     if random_number == 0:
//         computer_choice = "R"

//     elif random_number == 1:
//         computer_choice = "P"

//     elif random_number == 2:
//         computer_choice = "S"

//     // Print computer's choice
//     if computer_choice == "R":
//         print('The Computer chose rock.')

//     elif computer_choice == "P":
//         print('The Computer chose paper.')

//     elif computer_choice == "S":
//         print('The Computer chose Scissors.')


//     #Player wins
//     #Player: R    Computer: S
//     #Player: P    Computer: R
//     #Player: S    Computer: P

//     if (player_choice == "R" and computer_choice == "S") or \
//         (player_choice == "P" and computer_choice == "R") or \
//         (player_choice == "S" and computer_choice == "P"):
//         print("You win!")

//     # Computer wins
//     #Player: R    Computer: S
//     #Player: P    Computer: R
//     #Player: S    Computer: P

//     elif (player_choice == "P" and computer_choice == "S") or \
//         (player_choice == "S" and computer_choice == "R") or \
//         (player_choice == "R" and computer_choice == "P"):
//         print('You lose!')

//     // Set Tie

//     elif player_choice == computer_choice:
//         print('Tie!')

// print('''***************************************************************************
//                 Welcome to Rock, Paper, Scissors!

// The Rules:
// 1. You and the Computer will choose either Rock, Paper, or Scissors.
// 2. Rock beats scissors.
// 3. Paper beats rock.
// 4. Scissors beat paper.
// You are playing against a randomized computer, Best of Luck!
// ***************************************************************************''')
// while True: 
//     rps()
//     play_again = input('Would you like to play another round? [Y/N]').lower()
//     if play_again == 'n':
//         break
let start_btn = document.querySelector("#start_btn")
let RPS_Options = document.querySelector("#RPS_Options")
let output_div = document.querySelector("#output_div")
start_btn.addEventListener('click', function() {
    let player_choice = RPS_Options.value
    let rps_choice = ['R', 'P', 'S']

    function random_element(arr) {
        return arr[Math.floor(Math.random()*arr.length)]
    }
    // console.log(rps_choice)

    let computer_choice= random_element(rps_choice)
    console.log(computer_choice)
    console.log(player_choice)
    if (player_choice === 'R' && computer_choice === 'S'){
        output_div.innerText = 'Computer chose Scissors, You WIN!'
    }
    else if (player_choice === 'P' && computer_choice === 'R'){
        output_div.innerText = 'Computer chose Rock, You WIN!'
    }
    else if (player_choice === 'S' && computer_choice === 'P'){
        output_div.innerText = 'Computer chose Paper, You WIN!'
    }
    else if (player_choice === computer_choice){
        output_div.innerText = 'You have tied!'
    }
    else{
        output_div.innerText = `You chose ${player_choice}, and the computer chose ${computer_choice}, YOU LOSE!`
    }
})
