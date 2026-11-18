let n = 2;
let i = 0;
let count = 0;
while (i <= n) {
    if (n%i === 0) {
        count = count + 1
    }
    i = i + 1
}
if (n === 1) {
    console.log("Not Prime")
}
else{
    if (count > 2) {
        console.log("Not Prime")
    }
    else {
        console.log("Prime")
    }
}
