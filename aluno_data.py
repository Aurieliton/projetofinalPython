import pymysql.cursors
from aluno import Aluno

class AlunoData:
    def __init__(self):
        self.conexao = pymysql.connect(host='localhost',
                                       user='root',
                                       password='',
                                       database='escola',
                                       cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.conexao.cursor()

    def insert(self, aluno: Aluno):
        try:
            sql =  "INSERT INTO alunos VALUES (%s,%s,%s,%s,%s)"
            self.cursor.execute(sql,(aluno.matricula,
                                aluno.nome,
                                aluno.idade,
                                aluno.curso,
                                aluno.nota))
            self.conexao.commit()
        except Exception as error:
            print(f'Erroao Inserir! Erro: {error}')


    def select(self):
        try:
            sql= "SELECT * FROM alunos"
            self.cursor.execute(sql)
            alunos=self.cursor.fetchall()
            return alunos
        except Exception as error:
            print(f"Erro ao listar! Erro: {error} ")






    def update(self,alunos: Aluno):
        try:
            sql = "Update alunos SET nome= %s, idade= %s, curso= %s, nota= %s where matricula= %s"
            self.cursor.execute(sql,(alunos.nome,
                                          alunos.idade,
                                          alunos.curso,
                                          alunos.nota,
                                          alunos.matricula))
            self.conexao.commit()
        except Exception as error:
            print(f"Erro ao fazer alteração! Erro: {error} ")

    def delete(self,matricula:str):
        try:
            sql="DELETE FROM alunos WHERE matricula =%s"
            self.cursor.execute(sql,matricula)
            self.conexao.commit()
        except Exception as error:
            print(f'Erro ao deletar! Erro: {error}')



if __name__ == '__main__':
    ad = AlunoData()
    # alunos = Aluno('jonas', 21,'Python',9.2)
    # ad.insert(aluno)
    #print(ad.select())
    alunos = Aluno('Aurieliton',28,'java',10,)
    alunos.matricula = 'd8ad7615-8a55-11ee-9954-0ae0aff903cf'
    ad.update(alunos)
    alunos.matricula = 'd8ad7615-8a55-11ee-9954-0ae0aff903cf'
    ad.delete(alunos)
    print(ad.select())
