var shipWithinDays = function(weights, days) {
    function sum(weights){
        let total = 0;
        for(let num of weights){
            total += num;
        } 
        return total
    }
    
    function capacityCheck(weights,days,cap){
        let count = days;
        let sum = 0;
        for(let i = 0; i<weights.length ;i++){
            sum = sum + weights[i];
            if(sum>cap){
                count = count -1 
                sum = weights[i];
                
            }
            if(count<1){
                return false;
            }
            
        }
        return true
    }
    
    let i = Math.max(...weights);
    let j = sum(weights);
    let capacity = j;
    
    while(i<=j){
        let mid = Math.floor((i+j)/2);
        if(capacityCheck(weights,days,mid)){
            capacity=mid;
            j = mid-1;
        }
        else{
            i = mid+1;
        }
        
    }    
    
    return capacity

    
};


let weights =[1,2,3,1,1];
let days = 4;

let result = shipWithinDays(weights, days);
console.log(result);