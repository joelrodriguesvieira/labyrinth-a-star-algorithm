import express from "express";
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import cors from "cors";

const app = express();
const port = 3000;

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const corsOptions = {
  origin: "*",
  methods: "POST",
};

app.use(cors(corsOptions));

// Middleware para servir arquivos estáticos (index.html, style.css, index.js)
app.use(express.static(__dirname));

// Middleware para interpretar JSON no body
app.use(express.json());

// Rota que recebe a matriz e salva no arquivo JSON
app.post("/save-matrix", (req, res) => {
  const matrix = req.body;
  const savePath = path.join(__dirname, "labyrinth.json");

  fs.writeFile(savePath, JSON.stringify(matrix, null, 2), (err) => {
    if (err) {
      console.error("Erro ao criar o ficheiro:", err);
      return res.status(500).send("Erro ao salvar JSON");
    }

    console.log("Ficheiro JSON criado com sucesso!");
    res.send("JSON salvo com sucesso!");
  });
});

app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});
