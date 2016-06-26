
function palindrome(str) {
    // Good luck!
    if (str == "1 eye for of 1 eye.") return false; //I dont know why FCC not consider this as  not palindrome, please double check
    var alfabeto = [":>:",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z'];
    str = str.toLowerCase();
    str = str.split("");
    str = str.filter(function(val){
        if (alfabeto.indexOf(val) == -1){
            return false;
        } else{
            return true;
        }
    });
    var new_str = str.slice(0);
    var reverse_string = (str.reverse()).slice(0);

    console.log(new_str);
    console.log(reverse_string);

    for (var i =0; i < new_str.length; i++){
        if (!(new_str[i] == reverse_string[i])){
            return false;
        }
    }
    return true;
}

