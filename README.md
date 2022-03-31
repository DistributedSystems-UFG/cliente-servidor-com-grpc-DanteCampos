# Calculadora distribuída com gRPC

Servidor:
Disponibiliza as operações add(a,b), mult(a,b) e pow(a,b) para adição, multiplicação e potenciação.
Conexões são feitas pela porta 12345.

Cliente:
Chama operações add, mult e pow conectando na porta 12345 do servidor.
