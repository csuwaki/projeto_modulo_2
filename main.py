from view import userView

print(
    "Bem-vindo à API Bitbucket! Com esta API:  \n \
\n \
- Acesse informações públicas do usuário;  \n \
- Acesse repositórios públicos ou privados, tags ou branches;  \n \
- Crie, atualize ou exclua um de seus repositórios;  \n \
- Acesse, crie, atualize ou exclua um serviço; \n \
- Acesse, crie ou exclua uma chave SSH; \n \
- Baixe um repositório como um arquivo; \n \
- Acesse, crie, atualize ou exclua um problema; \n \
- Acesse, crie, atualize ou exclua um comentário. \n \
 \n \
Insira um termo de pesquisa: ")
user = userView()
user.set_user(input())
#perguntar em qual formato o usuário deseja a resposta
print(user.resposta())