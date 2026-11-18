// print the minimum number from a list
// if the list is none or empty print invalid
function minimun_no(arr){
    if (!arr || arr.length == 0){
        return "Invaild"
    }
    else{
        let min = arr[0]
        for (let i = 0; i < arr.length; i++){
            if (min<arr[i]){
                min = arr[i]
            }
        }
        return min
    }
}
arr = [10, 20 , 30, 40, 50, 60, 70, 100]
console.log(maximum_no(arr))