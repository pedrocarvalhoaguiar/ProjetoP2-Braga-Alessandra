# ProjetoP2-Braga-Alessandra
 
## 1. Deivid Hugo dos Santos Ramos – 202022731
## 2. Almir de Souza Pontes Junior – 202021932
## 3. Pedro Carvalho Aguiar – 202022339
## 4. Wanderson Rosa Thimoteo – 202021928
## 5. Rodrigo Figueiredo Costa de Oliveira – 202022177
## 6. Renan Alves de Oliveira – 202022207
## 7. Adriana Santos Pereira – 202021922
## 8. Rafael Alves Pinheiro – 202021930

- Sistema para cadastro de pessoas de rua vacinadas. Uma vez que uma pessoa de rua raramente tem identidade ou vai guardar caderneta de vacinação e coisas assim, seria importante armazenar dados significativos para poder encontrar a pessoa novamente ou identificá-la se reencontrá-la. 
- Assuma que será possível usar Biometria, então, vamos simular a biometria através de um arquivo. Assim que a pessoa for inserida no sistema, o seu programa deve gerar um arquivo, que pode ser feito de 255 linhas com 255 números separados por vírgulas. Essa geracao é meramente para demonstracao entoa vcs podem repetir os codigos de identidade do usuário ou algo assim.
- O sistema deve armazenar as pessoas em um arquiv.
- O sistema deve permitir buscas rápidas entao deve manter os usuários na memória em uma árvore binária
- Sistema para cadastro de pessoas de rua vacinadas. Uma vez que uma pessoa de rua raramente tem identidade ou vai guardar caderneta de vacinação e coisas assim. Seria importante poder encontrar a pessoa novamente ou identificá-la se reencontrá-la. Assuma que será possível usar Biometria, então, vamos simular a biometria através de um arquivo. 
Esse arquivo (que vamos criar de forma simulada) pode ser feito de 255 linhas com 255 números separados por vírgulas. 
- O programa deve criar uma árvore binária (ordenada) onde cada linha do arquivo seria armazenada em um nó da árvore. 
- Se o sistema quisesse comparar a biometria de uma pessoa qualquer com a biometria (outro arquivo) de um desconhecido, ele iria lendo esse novo arquivo e para cada linha ele iria procurar na árvore, se encontar pelo menos umas 40 linhas iguais ele daria um match.