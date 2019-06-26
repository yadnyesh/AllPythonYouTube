import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.posts
posts = db.posts
post_data = {
    'title': 'Python and MongoDB Not my Own',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))
post_1 = {
    'title': 'Python and MongoDB New',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}
new_result = posts.insert_many([post_1, post_2, post_3])
print('Multiple posts: {0}'.format(new_result.inserted_ids))

bills_post = posts.find_one({'author': 'Bill'})
print(bills_post)