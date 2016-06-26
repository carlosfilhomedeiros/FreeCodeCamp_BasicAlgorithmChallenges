
function findLongestWord(str) {
    str = str.split(" ");
    var old = 0;
    for (var i =0; i< str.length; i++){
        if (old < str[i].length){
            old = str[i].length;
        }
    }
    return old;
}
