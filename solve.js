let board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3]
];

function findEmpty(board){
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[i].length; j++) {
            if (board[i][j] == 0){
                return [i, j];
            }
        }  
    }
    return false;
}

function solve(board){
    let find = findEmpty(board);
    if (!find){
        return true;
    }

    let [row, col] = find;

    for (let i = 1; i < 10; i++) {
        if (checkNum(board, i, row, col)){
            board[row][col] = i;

            if (solve(board)){
                return true;
            }
            board[row][col] = 0;
        }
    }
    return false;
}

function checkNum(board, i, row, col){
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


function printBoard(board){
    for (let i = 0; i < board.length; i++) {
        if (i % 3 == 0 && i != 0)
            console.log("- - - - - - - - - - - -");

        for (let j = 0; j < board.length; j++) {
            if (j % 3 == 0 && j != 0)
                console.log("|", " ")

            if (j === 8)
                console.log(board[i][j]);

            else
                console.log(board[i][j], " ")
            
        }

    }
}

solve(board);
printBoard(board);

