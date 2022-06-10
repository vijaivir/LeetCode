/**
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
    var parentheses = []
    for(var i = 0; i < s.length; i++){
        if(s[i] === "("){
            parentheses.push(s[i])
        }else if(s[i] === "["){
            parentheses.push(s[i])
        }else if(s[i] === "{"){
            parentheses.push(s[i])
        }else if(s[i] === ")"){
            if(parentheses.pop() !== "("){
                    return false
                }
        }else if(s[i] === "]"){
            if(parentheses.pop() !== "["){
                    return false
                }
        }else if(s[i] === "}"){
            if(parentheses.pop() !== "{"){
                    return false
                }
        }
    }
        
    if(parentheses.length > 0){
        return false
    }

    return true
};