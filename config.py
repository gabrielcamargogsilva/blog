ambiente = 'teste' #TESTE OU PRODUÇÃO

if ambiente == 'teste':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'blog'

if ambiente == 'producao':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'gabrielcamargog.mysql.pythonanywhere-services.com'
    DB_USER = 'gabrielcamargog'
    DB_PASSWORD = 'gcgs@804041.python'
    DB_NAME = 'gabrielcamargog$default'

#CONFIG CHAVE SECRETA DE SESSÃO
SECRET_KEY = 'blog'

#SENHA DO ADM 
MASTER_EMAIL = "gabrielcamargo@adm"
MASTER_PASSWORD = "adm123"