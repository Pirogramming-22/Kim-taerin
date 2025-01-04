let timerInterval;
let elapsedTime = 0;
const timeBox = document.querySelector('.time_box');
const startButton = document.getElementById('start');
const stopButton = document.getElementById('stop');
const resetButton = document.getElementById('reset');
const recordBox = document.querySelector('.record_bottom');
const deleteAllButton = document.querySelector('.trash_botton');

// 시간 포맷팅 함수
function formatTime(ms) {
    const totalSeconds = Math.floor(ms / 1000);
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    const milliseconds = ms % 1000;
    return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}.${String(Math.floor(milliseconds / 10)).padStart(2, '0')}`;
}

// 타이머 업데이트 함수
function updateTimer() {
    timeBox.textContent = formatTime(elapsedTime);
}

// 타이머 시작
function startTimer() {
    if (timerInterval) return; // 이미 타이머가 실행 중인 경우 중복 실행 방지
    const startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(() => {
        elapsedTime = Date.now() - startTime;
        updateTimer();
    }, 10);
}

// 타이머 중지
function stopTimer() {
    if (!timerInterval) return; // 타이머가 실행 안하면 작업도 안함 
    clearInterval(timerInterval);
    timerInterval = null;
    addRecord(); // 기록 추가
}

// 타이머 리셋
function resetTimer() {
    clearInterval(timerInterval);
    timerInterval = null;
    elapsedTime = 0;
    updateTimer();
}

// 기록 추가 함수
function addRecord() {
    const recordItem = document.createElement('li');
    recordItem.textContent = formatTime(elapsedTime);

    const deleteButton = document.createElement('button');
    deleteButton.textContent = '삭제';
    deleteButton.classList.add('delete-button');
    deleteButton.addEventListener('click', () => {
        recordItem.remove();
    });

    recordItem.appendChild(deleteButton);
    recordBox.appendChild(recordItem);
}

// 모든 기록 삭제 함수
function deleteAllRecords() {
    if (recordBox.children.length === 0) return; // 기록 없으면 아무 것도 안함함
    const confirmDelete = confirm('모든 기록을 삭제하시겠습니까?');
    if (confirmDelete) {
        recordBox.innerHTML = ''; 
    }
}

// 이벤트 리스너 등록
startButton.addEventListener('click', startTimer);
stopButton.addEventListener('click', stopTimer);
resetButton.addEventListener('click', resetTimer);
deleteAllButton.addEventListener('click', deleteAllRecords);

updateTimer();
