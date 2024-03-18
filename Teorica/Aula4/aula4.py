from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017', )

db = client['countries']

paises = db.countries

# result = paises.insert_one({
#     'name': 'Brasil',
#     'temp':{
#         'SP': 26,
#         'RJ': 32,
#         'MG': 26
#     }
# })

# if result.acknowledged:
#     print('Documento adicionado!')
# else:
#     print('Erro')

# result = paises.update_one(
#     {'temp.MG':{'$exists':True}},
#     {'$set':{'temp.MG':30}}
# )

# if result.acknowledged:
#     print('Documento atualizado!')
# else:
#     print('Erro')

# result = paises.delete_one({'name':'Brasil'})
# if result.acknowledged:
#     print('Documento removido!')
# else:
#     print('Erro')



result = paises.find()

for aux in result:
    print(aux)