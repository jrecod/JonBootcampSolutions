//define the password possibilities
let alphabet_lower='abcdefghijklmnopqrstuvwxyz'
let alphabet_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
let nums='1234567890'
let spec_char=',./;[]{}<>?!@#$%^&*()_+-='
//prompt user on their password needs
// let pw_length = Number(prompt('How long does the password need to be? '))
let lower_count= Number(prompt('How many lower case? '))
let upper_count= Number(prompt('How many upper case? '))
let nums_count= Number(prompt('How many numbers? '))
let spec_count= Number(prompt('How many special characters? '))

let password=''

for(let i=0; i<lower_count; ++i){
    let random_number= Math.floor(Math.random() * alphabet_lower.length)
    password+=(alphabet_lower[random_number])
}
for(let i=0; i<upper_count; ++i){
    let random_number= Math.floor(Math.random() * alphabet_upper.length)
    password+=(alphabet_upper[random_number])
}
for(let i=0; i<nums_count; ++i){
    let random_number= Math.floor(Math.random() * nums.length)
    password+=(nums[random_number])
}
for(let i=0; i<spec_count; ++i){
    let random_number= Math.floor(Math.random() * spec_char.length)
    password+=(spec_char[random_number])
}
// console.log(password)
let new_array=password.split('')
for(let i=0; i<password.length; ++i){
    let random_number= Math.floor(Math.random() * new_array.length)
    let password_tmp=new_array[i]
    new_array[i]=new_array[random_number]
    new_array[random_number]=password_tmp
}
console.log(new_array.join(''))
