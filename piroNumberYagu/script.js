let attempts = 9; 
const attemptsDOM = document.getElementById("attempts"); 
attemptsDOM.innerText = attempts; 
// 시도 횟수 초기화화화

let answer = []; 
// 배열 만듦듦
while (answer.length < 3) {
    const num = Math.floor(Math.random() * 10);
    if (!answer.includes(num)) {
        answer.push(num);
    }
}

document.getElementById('results').innerHTML = ''; 
document.getElementById('game-result-img').src = ''; 
document.getElementById('number1').value = ''; 
document.getElementById('number2').value = ''; 
document.getElementById('number3').value = ''; 
document.querySelector('.submit-button').disabled = false;

function check_numbers() {
    const num1 = document.getElementById('number1').value;
    const num2 = document.getElementById('number2').value;
    const num3 = document.getElementById('number3').value;

    
    if (!num1 || !num2 || !num3) {
        document.getElementById('number1').value = '';
        document.getElementById('number2').value = '';
        document.getElementById('number3').value = '';
        return;
    }
// 비교 연산자 써서 숫자 각각 비교 
    const guess = [parseInt(num1), parseInt(num2), parseInt(num3)];

    let strikes = 0;
    let balls = 0;

    for (let i = 0; i < 3; i++) {
        if (guess[i] === answer[i]) {
            strikes++;
        } else if (answer.includes(guess[i])) {
            balls++;
        }
    }

    let resultText = '';
    if (strikes === 3) {
        resultText = '3 S 0 B';
        document.getElementById('game-result-img').src = 'success.png';
        document.querySelector('.submit-button').disabled = true;
    } else if (strikes === 0 && balls === 0) {
        resultText = 'O';
    } else {
        resultText = `${strikes} S ${balls} B`;
    }


    const resultDiv = document.getElementById('results');
    const resultItem = document.createElement('div');
    resultItem.textContent = resultText;
    resultDiv.appendChild(resultItem);

    attempts--;
    attemptsDOM.innerText = attempts;

    if (attempts === 0 && strikes !== 3) {
        document.getElementById('game-result-img').src = 'fail.png';
        document.querySelector('.submit-button').disabled = true;
    }
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
}

