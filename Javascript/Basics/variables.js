var a = 10 ; //var for global scopping

let b = 20 ; //let for block scopping

const c =10 ; // const for constants

/*
Variable Assignment and Re-assignment
Variables declared with var and let can be
reassigned new values, while variables declared with
const cannot. 
*/


var message = "Hello, Geeks!";
message = "Hello, GeeksforGeeks!";
console.log(message); // Outputs: Hello, GeeksforGeeks!

let text = "JavaScript is the best!";
text = "JavaScript is awesome!";
console.log(text); // Outputs: JavaScript is awesome!

const number = 10;
// number = 20; // Error: Assignment to constant variable.

/**
 * Why Use let and const over var?
Block Scoping: let and const are block-scoped, 
meaning they are only accessible within the block they are defined. var is function-scoped, which can lead to unexpected behavior.
Re-assignment: const ensures that variables
 cannot be reassigned, which helps prevent accidental 
 changes to important values.

 */

 let message2= "Hello, Geeks!";
console.log(message2); // Outputs: Hello, Geeks!
message2 = "Hello, GeeksforGeeks!";
console.log(message2); // Outputs: Hello, GeeksforGeeks!

const year = 2024;
console.log(year); // Outputs: 2024
// year = 2025; // Error: Assignment to constant variable.