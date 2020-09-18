Problem 4
Write a function that returns the number of occurances of 'hi' in a given string.

function count_hi(text){
    let accumulator = 0
    for(let i = 0; i < text.length-1; ++i){
        if(text[i] == 'h' && text[i+1] == 'i'){
            ++ accumulator
        }
    }
    return accumulator
}

  
console.log(count_hi('hihihihihihi'))  //6

Problem 5
Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

function snake_case(text){
    let spec_chars = String.raw`!@#$%^&*\(\)_+{}:\?,\.\/;'[]\\-='`
    // console.log(spec_chars)
    let tmp_string = text.toLowerCase()
    let tmp_string2 = ""
    for (let i=0; i<tmp_string.length; ++i) {
        if (spec_chars.indexOf(tmp_string[i]) == -1) {
            tmp_string2 += tmp_string[i]            
        }
    }
    // console.log(tmp_string)
    while (tmp_string2.indexOf(" ") != -1) {
        tmp_string2 = tmp_string2.replace(" ", "_")
    }
    // console.log(tmp_string)
    return tmp_string2
}
    // snake_case("Hello World!")
console.log(snake_case('Hello World!')) // hello_world
console.log(snake_case('This is another example.')) // this_is_another_example


Problem 6
Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

function camel_case(text) {
    let spec_chars = String.raw`!@#$%^&*\(\)_+{}:\?,\.\/;'[]\\-='`
        // console.log(spec_chars)
        let tmp_string = text.toLowerCase()
        let tmp_string2 = ""
        for (let i=0; i<tmp_string.length; ++i) {
            if (spec_chars.indexOf(tmp_string[i]) == -1) {
                tmp_string2 += tmp_string[i]            
            }
        }
        while (tmp_string2.indexOf(" ") != -1) {
        let index = temp_string2.indexOf(" ")
    }
}
console.log(camel_case('Hello World!')) // helloWorld
console.log(camel_case('This is another example.')) // thisIsAnotherExample










































// Problem 7
// Write a function that converts text to alternating case.

// function alternating_case(text){

// }







// console.log(alternating_case('Hello World!')) // HeLlO WoRlD!
// console.log(alternating_case('This is another example.')) // ThIs iS AnOtHeR ExAmPle.