function solution(participant, completion) {
    
    var comp = completion.length;
    var i;
    participant.sort();
    completion.sort();
    var answer = participant[participant.length-1];
    console.log(participant);
    console.log(completion);
    
    for(i= 0; i<comp ; i++){
        if(completion[i] != participant[i]){
            answer = participant[i];
            return answer;
        }
    }
    return answer;
}