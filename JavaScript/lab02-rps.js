let start_btn = document.querySelector("#start_btn")
let RPS_Options = document.querySelector("#RPS_Options")
let output_div = document.querySelector("#output_div")
start_btn.addEventListener('click', function() {
    let player_choice = RPS_Options.value
    let rps_choice = ['Rock', 'Paper', 'Scissors']

    function randomElement(arr) {
        return arr[Math.floor(Math.random()*arr.length)]
    }
    // console.log(rps_choice)

    let computer_choice= randomElement(rps_choice)
    // console.log(computer_choice)
    // console.log(player_choice)
    if (player_choice === 'Rock' && computer_choice === 'Scissors'){
        output_div.innerText = 'Computer chose Scissors, You WIN!'
    }else if (player_choice === 'Paper' && computer_choice === 'Rock'){
        output_div.innerText = 'Computer chose Rock, You WIN!'
    }else if (player_choice === 'Scissors' && computer_choice === 'Paper'){
        output_div.innerText = 'Computer chose Paper, You WIN!'
    }else if (player_choice === computer_choice){
        output_div.innerText = 'You have tied!'
    }else{
        output_div.innerText = `You chose ${player_choice}, and the computer chose ${computer_choice}, YOU LOSE!`
    }
})
