const gridContainer = document.getElementById("grid");
const sizeRange = document.getElementById("sizeRange");
const sizeLabel = document.getElementById("sizeLabel");
const sizeLabel2 = document.getElementById("sizeLabel2");
const btnRandom = document.getElementById("btn_random");
const btnConclude = document.getElementById("btn_conclude");
let gridSize = parseInt(sizeRange.value);
let gridData = [];

sizeRange.addEventListener("input", () => {
  gridSize = parseInt(sizeRange.value);
  sizeLabel.textContent = gridSize;
  sizeLabel2.textContent = gridSize;
  generateEmptyGrid();
});

btnRandom.addEventListener("click", () => {
  randomizeMaze();
});

btnConclude.addEventListener("click", () => {
  finalizar();
});

function generateEmptyGrid() {
  gridContainer.innerHTML = "";
  gridContainer.style.gridTemplateColumns = `repeat(${gridSize}, 30px)`;
  gridData = [];

  for (let row = 0; row < gridSize; row++) {
    let rowData = [];
    for (let col = 0; col < gridSize; col++) {
      const cell = document.createElement("div");
      cell.className = "cell";

      if (row === 0 && col === 0) {
        cell.classList.add("start");
        cell.textContent = "S";
        rowData.push(1);
      } else if (row === gridSize - 1 && col === gridSize - 1) {
        cell.classList.add("end");
        cell.textContent = "E";
        rowData.push(1);
      } else {
        cell.classList.add("floor");
        rowData.push(1);
      }

      gridContainer.appendChild(cell);
    }
    gridData.push(rowData);
  }
}

function isValidPosition(row, col) {
  return row >= 0 && row < gridSize && col >= 0 && col < gridSize;
}

function isSurroundedByWalls(row, col, tempData) {
  const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  return directions.every(([dr, dc]) => {
    const r = row + dr;
    const c = col + dc;
    return !isValidPosition(r, c) || tempData[r][c] === null;
  });
}

function randomizeMaze() {
  gridContainer.innerHTML = "";
  gridContainer.style.gridTemplateColumns = `repeat(${gridSize}, 30px)`;
  gridData = [];

  for (let row = 0; row < gridSize; row++) {
    let rowData = [];
    for (let col = 0; col < gridSize; col++) {
      rowData.push(null);
    }
    gridData.push(rowData);
  }

  for (let row = 0; row < gridSize; row++) {
    for (let col = 0; col < gridSize; col++) {
      const cell = document.createElement("div");
      cell.className = "cell";

      if (row === 0 && col === 0) {
        cell.classList.add("start");
        cell.textContent = "S";
        gridData[row][col] = 1;
      } else if (row === gridSize - 1 && col === gridSize - 1) {
        cell.classList.add("end");
        cell.textContent = "E";
        gridData[row][col] = 1;
      } else {
        const rand = Math.random();
        if (rand < 0.40) {
          // Parede (40%)
          gridData[row][col] = null;
        } else if (rand < 0.60) {
          cell.classList.add("floor");
          gridData[row][col] = 1;
        } else if (rand < 0.80) {
          cell.classList.add("forest");
          gridData[row][col] = 2;
        } else {
          cell.classList.add("mud");
          gridData[row][col] = 3;
        }
        

        if (gridData[row][col] === null) {
          if (isSurroundedByWalls(row, col, gridData)) {
            cell.classList.add("floor");
            gridData[row][col] = 1;
          } else {
            cell.classList.add("wall");
            cell.textContent = "#";
          }
        }
      }

      gridContainer.appendChild(cell);
    }
  }
}

function finalizar() {

  const symbolMap = {
    1: ".",
    2: "?",
    3: "_",
    null: "#",
  };

  const symbolMatrix = gridData.map((row, rowIndex) =>
    row.map((cell, colIndex) => {
      if (rowIndex === 0 && colIndex === 0) return "S";
      if (rowIndex === gridSize - 1 && colIndex === gridSize - 1) return "E";
      return symbolMap[cell];
    })
  );

  fetch("http://localhost:3000/save-matrix", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(symbolMatrix),
  })
    .then((response) => response.text())
    .then((message) => {
      alert(message);
    })
    .catch((error) => {
      console.error("Erro ao enviar JSON:", error);
    });
}

generateEmptyGrid();
