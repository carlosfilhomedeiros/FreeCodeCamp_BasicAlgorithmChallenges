function reverseString(str) {
    var str2Array = str.split("");
    str = str2Array.reverse();
    str = str.join("");
    return str;
}

reverseString("Hello");
