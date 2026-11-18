function count(lst, n){
    if (!lst) {
        return "Invalid"
    }
    else{
        let count = 0
        for (let i = 0; i<lst.length; i++){
            if (lst[i] === n) {
                count++
            }
            
        }
        return count
    }
}
lst = null
n = 10
console.log(count(lst, n))