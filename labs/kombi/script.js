// você é um(a) hacker =)

const wordToGuess = 'MOTRIZ'.toUpperCase();
const gridRows = 6;
let currentRow = 0;
let currentCol = 0;

function createGrid() {
    const grid = document.getElementById('wordleGrid');
    for (let i = 0; i < gridRows * 6; i++) {
        let cell = document.createElement('div');
        cell.classList.add('grid-cell');
        cell.setAttribute('id', 'cell' + i);
        cell.contentEditable = true;
        cell.oninput = () => handleInput(cell);
        cell.onkeydown = (e) => handleKeyPress(e, cell);
        grid.appendChild(cell);
    }
}

function handleInput(cell) {
    if (cell.textContent.length > 1) {
        cell.textContent = cell.textContent.slice(-1); // Keep only the last character
    }
    moveToNextCell(cell);
}

function handleKeyPress(e, cell) {
    if (e.key === 'Enter') {
        e.preventDefault(); // Prevent default Enter key behavior
        submitGuess();
    } else if (e.key === 'Backspace' && cell.textContent === '') {
        moveToPreviousCell(cell);
    }
}

function moveToNextCell(currentCell) {
    let nextCell = currentCell.nextSibling;
    if (nextCell && currentCell.textContent.trim() !== '') {
        nextCell.focus();
    }
}

function moveToPreviousCell(currentCell) {
    let prevCell = currentCell.previousSibling;
    if (prevCell) {
        prevCell.focus();
    }
}

function submitGuess() {
    let guess = '';
    for (let i = 0; i < 6; i++) {
        guess += document.getElementById('cell' + (currentRow * 6 + i)).textContent.toUpperCase();
    }
    if (guess.length !== 6) {
        alert('Please enter a 6 letter word.');
        return;
    }
    updateGrid(guess);
    currentRow++;
    if (currentRow < gridRows) {
        document.getElementById('cell' + (currentRow * 6)).focus();
    }
}

function updateGrid(guess) {
    for (let i = 0; i < guess.length; i++) {
        let cell = document.getElementById('cell' + (currentRow * 6 + i));
        if (wordToGuess[i] === guess[i]) {
            cell.classList.add('correct');
        } else if (wordToGuess.includes(guess[i])) {
            cell.classList.add('present');
        } else {
            cell.classList.add('absent');
        }
    }

    if (guess === wordToGuess) {
        alert('Parabéns! Você acertou!.');
    } else if (currentRow === gridRows - 1) {
        alert('Fim de jogo! Recarrege a página para tentar de novo' );
    }
}

createGrid();
document.getElementById('cell0').focus();
