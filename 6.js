function union(array1, array2){
    var unionArray = []
    for (var i of array1){
        unionArray.push(i)
    }
    for (var j of array2){
        if (!unionArray.includes(j)){
            unionArray.push(j)
        }
    }
    
    return unionArray.sort((a,b)=>{
        return a-b
    })
}

console.log(union([1, 2, 3], [100, 2, 1, 10]));