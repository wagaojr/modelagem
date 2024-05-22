% Questão 5 do primeiro trabalho de Modelagem de Sistemas Dinâmicos
% Wagner Junior
% Segunda forma de Equação de Estados de H(s), por similaridade
clear all

A = [0 1; -100 -0.2]; % matriz A
B = [0; 1]; % matriz B
C = [-525 -1.25]; % matriz C
D = 6.25; % matriz D

% Função de transferência           
% Conversão para função de transferência

Co = ctrb(A, B);
rank_Co = rank(Co);

if rank_Co == size(A, 1)
    disp('O sistema é controlável.');
else
    disp('O sistema não é controlável.');
    return;
end

% Matriz de transformação T (inversa da matriz de controlabilidade)
T = [4 3; 1 2];

% Forma controlável das matrizes
A_cont = T * A * inv(T);
B_cont = T * B;
C_cont = C * inv(T);
D_cont = D;

% Exibição das novas matrizes de estado
disp('Matriz A na forma controlável:');
disp(A_cont);

disp('Matriz B na forma controlável:');
disp(B_cont);

disp('Matriz C na forma controlável:');
disp(C_cont);

disp('Matriz D na forma controlável:');
disp(D_cont);

sys = ss(A_cont, B_cont, C_cont, D_cont);  % Criação do sistema de estado
H = tf(sys);

% Exibição da função de transferência
disp('A função de transferência do sistema é:');
H
step(H)