% -------------------------------------------------------------------------
% LABORATORIO DI ELABORAZIONE DI IMMAGINI MEDICHE - A.A. 2017/18
% -------------------------------------------------------------------------
clear all
close all
clc

% 1. Lettura file DICOM e dimensione di ogni frame
file = dicomread(...

% 2. Info del file
info = dicominfo(...

% 3. Rimozione dimensioni singole e imshow3D
cineloop = squeeze(...

% 4. Estrazione 40° frame, istogramma luminosità e colorbar
I = ...

% 5A. Equalizzazione mediante funzione Matlab
I_eq = histeq(...

% 5B. Equalizzazione mediante cambiamento della colormap
...              

% 5C. Plot delle due colormap e confronto pixel 
figure(), ...

% 6. Scrittura img su file DICOM
dicomwrite(...