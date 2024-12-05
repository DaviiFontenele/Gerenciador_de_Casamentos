"""
me deparei com o seguinte erro:

C:\Users\Dr Andre\AppData\Local\Programs\Python\Python313\python.exe: can't open file 'C:\\Users\\Dr Andre\\Documents\\MeusProjetos\\Gerenciador_de_Casamentos\\manage.py': [Errno 2] No such file or directory. 

a solução foi:

ajustar o novo caminho:
cd "C:\Users\Dr Andre\Documents\MeusProjetos\Gerenciador_de_Casamentos\Gerenciador_de_Casamento"
cd "C:\Users\Dr Andre\Documents\MeusProjetos\Gerenciador_de_Casamentos\Gerenciador_de_Casamento\Gerenciador de casamentos"

e apos rodar o comando:

python manage.py runserver

"""

"""
2) erro 02

nao foi instalada a biblioteca Pillow

para isso:

python -m pip install Pillow


"""