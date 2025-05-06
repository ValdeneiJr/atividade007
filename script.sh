#!/bin/bash

# Limpa ou cria o arquivo de saída
echo "Saídas da atividade 007" > saidas.txt
echo "==========================" >> saidas.txt

# Executa cada script Python
for i in $(seq -w 1 10); do
    script="at007_questao${i}.py"
    echo -e "\n>>> Questão $i" >> saidas.txt
    python3 "$script" >> saidas.txt
done

echo -e "\nExecução concluída. Saídas salvas em saidas.txt"

