/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function(s) {
    let stack = [s[0]];
    var i = 1;
    while(i < s.length){
        if(s[i] == stack[stack.length - 1]){
            stack.pop();
        }
        else{
            stack.push(s[i]);
        }
        i++;
    }
    var answer = "";
    for(let letter of stack){
        answer += letter;
    }
    
    return answer
    
};