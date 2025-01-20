var minEatingSpeed = function(piles, h) {
    
    function checkBananaRate(piles,mid,h){
    
        let hrs = 0
        for(let i =0;i<piles.length;i++){
            hrs += Math.ceil(piles[i]/mid)
        }
        if (hrs>h){
            return false;
        }
        else{
            return true;
        }
    }
    
    let  i = 1;
    let j = Math.max(...piles);
    let minban = j
    
    while(i<=j){
        let mid = Math.floor((i+j)/2);
        if(checkBananaRate([...piles],mid,h)){
            if(mid<minban){
                minban = mid;
                j=mid-1;
            }
            else{
                i=mid +1;
            }
        }
        else{
            i = mid +1
            }
        }
    return minban;
};


let piles = [30,11,23,4,20];
let h = 5;
result = minEatingSpeed(piles, h)
console.log(result)