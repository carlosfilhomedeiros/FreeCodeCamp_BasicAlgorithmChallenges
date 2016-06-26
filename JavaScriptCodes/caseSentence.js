
function titleCase(str) {
    str = str.toLowerCase();
    str = str.split(" ");
    var str2 = str.map(function(val){
        val = val.split("");
        val.unshift(val.shift().toUpperCase());
        val = val.join("");
        return val;
    });
    return str2.join(" ");

}
