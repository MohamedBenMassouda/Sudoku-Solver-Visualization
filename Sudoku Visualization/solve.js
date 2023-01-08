let board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]


function getArray(board){
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++){
            const cell = document.getElementById(`cell${i}-${j}`);
            cell.innerText = board[i][j];
        }   
    }
}

function findEmpty(board){
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[i].length; j++) {
            const cell = document.getElementById(`cell${i}-${j}`);
            if (cell.innerText == 0){
                return [i, j];
            }
        }  
    }
    return false;
}

async function solve(board){
    let find = findEmpty(board);
    if (!find){
        return true;
    }

    let [row, col] = find;
    const cell = document.getElementById(`cell${row}-${col}`);

    for (let i = 1; i < 10; i++) {
        // Highlight the current cell
        cell.style.backgroundColor = "yellow";
        if (checkNum(board, i, row, col)){
            board[row][col] = i;
            cell.innerText = i;
            
            if (await solve(board)){
                cell.style.backgroundColor = "green";
                return true;
            }
            // Reset the cell if the current number doesn't work
            cell.innerText = 0;
            board[row][col] = 0;
            // Highlight the cell in red to show that it was reset
            cell.style.backgroundColor = "red";
        }
        // Add a delay of 10 milliseconds between each iteration
        await new Promise(resolve => setTimeout(resolve, 30));
        // Reset the cell's background color
        cell.style.backgroundColor = "white";
    }
    return false;
}

function checkNum(board, i, row, col){
    const cell = document.getElementById(`cell${row}-${col}`);
    // Checking Row
    for (let j = 0; j < board.length; j++) {
        if (board[j][col] === i && j != row){
            return false;
        }
    }

    // Checking Col
    for (let j = 0; j < board.length; j++) {
        if (board[row][j] === i && j != col){
            return false;
        }
    }
    
    //Checking 3x3
    let box_x = Math.floor(col / 3);
    let box_y = Math.floor(row / 3);

    for (let j = box_y * 3; j < box_y * 3 + 3; j++) {
        for (let k = box_x * 3; k < box_x * 3 + 3; k++) {
            if (board[j][k] === i && j != row && k != col){
                return false;
            }
        }
    }

    return true;
}

