async function main(){

    async function nestedIntoPlain(array){
        var output = []
        for (var i of array){
            if (typeof(i)=="number"){
                output.push(i)
        }else{
            var n = await nestedIntoPlain(i)
            output.push(...n)
        }
    }
    return output
}
async function difference(array1,array2){
    var plainarray1 = await nestedIntoPlain(array1)
    var plainarray2 = await nestedIntoPlain(array2)
    var unique = []
    for (var i of plainarray1){
        
        if (!unique.includes(i)){
            unique.push(i)
        }
    }
    
    for (var i of plainarray2){
        
        if (!unique.includes(i)){
            unique.push(i)
        }
    }
    return unique
}


console.log(await difference([1, 2, 3, 4, 5], [1, [2], [3, [[4]]],[5,6]]));
}
main()