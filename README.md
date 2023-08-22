# Physics_ML_1
Um repositório para fins de estudo de MachineLearning em Python.

A proposta deste repositório é apresentar um estudo bastante elementar de Machine Learning usando-se de conceitos físicos. Inicialmente, tomando-se uma partícula sujeita apenas à gravidade, e portando uma velocidade vertical fixa, o computador varre um rol de velocidades distintas na horizontal (eixos x e z), a fim de buscar uma velocidade que melhor encaixe ao modelo, de forma que a distância entre ambas partículas se minimizem (*).

Este estudo foi inicialmente desenvolvido visando a aplicação em um modelo laboratorial prático: o resultado final deste programa é submetido a um pequeno robô lançador controlado via Arduíno, e os inputs que este robô recebe dependem diretamente dos resultados finais oferecidos por este programa, com algumas variações: este programa é meramente visual, não é o programa completo utilizado no projeto; grandezas como resistividade do ar não foram incluídas no projeto (**).

Este projeto é extremamente simples no ramo do Machine Learning, entretanto, foi um dos primeiros que eu desenvolvi, espero que seja do agrado de quem está o consultando! :)

(*): Se você quiser adicionar um elemento "vento" na simulação, basta alterar o segundo valor no return da função phys_env(), na linha 19 do arquivo functions_ctes.py. Eu particularmente recomendo que se troque o valor da aceleração no eixo Z, assim, você consegue um efeito um pouco mais interessante. (**): Se você busca incluir forças como resistividade do ar, talvez seja interessante aplicar a seguinte função: a = a - (0.01 * mag(v) * mag(v)) nas linhas 33 e 56 do arquivo main.py. O valor -0.01 é meramente empírico, com dependência geométrica/aerodinâmica. Fique a vontade para alterá-lo!
