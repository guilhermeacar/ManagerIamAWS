# Manager IAM for AWS

Script em python para gestão do IAM da AWS.

## Installation

Instalar o python versão 3

```bash
apt-get install python3
```
ou

```bash
yum install python3
```

Utilizar o package manager [pip](https://pip.pypa.io/en/stable/) para instalar o pip3.

```bash
pip3 install boto3
```

## Usage

Criar as váriaveis de ambiente, contendo a Access Key e Secret Key do seu usuário no IAM:
```bash
export AWS_ACCESS_KEY_ID="your access key"
export AWS_SECRET_ACCESS_KEY="your secret key"
```
Executar o script da seguinte forma:
```bash
python3 main.py
```
Será exibido o menu abaixo, para selecionar a função desejada:


```bash
------------------------------ MANAGER IAM AWS ------------------------------
1. Create group ReadOnly and Admin 
2. Create User 
3. Disable User 
4. Report All Users 
5. Exit 
-------------------------------------------------------------------------
Enter your choice [1-4]: 
```
1 - Cria os grupos ReadOnly e Admin, cada um com as respectivas policies do IAM atrelados. É necessário fornecer o Account Id da sua conta AWS.\
2 - Cria um usuário com a senha específicada e o adiciona ao grupo ReadOnly ou Admin.\
3 - Remove o logon no console da AWS do usuário informado.\
4 - Criar um relatório exibindo todos os usuários e o estado do dispositivo MFA.\
5 - Saída do script.
