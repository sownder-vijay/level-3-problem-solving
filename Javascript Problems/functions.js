//1. Write a function to find the square of a number using a function declaration.
//Named Function
function square_root(){
    return n * n
}
n = 10
console.log(square_root(n))

//Function Expression
const square = function(n){
    return n*n
}
console.log(square(20))

//Arrow Function
const sq = n => n*n
console.log(sq(30))

// 2. Write an arrow function to find the largest of two numbers.
let a = 10
let b = 20
const large = (a,b) => {if (a>b){return a} else{return b}}
console.log(large(a,b))

// Declare an array of positive numbers, filter out all the odd numbers and add a constant 2 to it.
let arr = [1, 2, 3, 4, 5, 6, 7]
let add_num = arr.filter(a => a%2 != 0).map(a => a+2);
console.log(add_num)