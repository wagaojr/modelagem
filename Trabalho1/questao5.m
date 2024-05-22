% Questão 5 do primeiro trabalho de Modelagem de Sistemas Dinâmicos
% Wagner Junior
% Equação de Estados de H(s)

% Definição das matrizes de estado
A = [0 1; -100 -0.2]; % matriz A
B = [0; 1]; % matriz B
C = [-525 -1.25]; % matriz C
D = 6.25; % matriz D

% Função de transferência
sys = ss(A, B, C, D);  % Criação do sistema de estado
H = tf(sys);           % Conversão para função de transferência

% Exibição da função de transferência
disp('A função de transferência do sistema é:');
H