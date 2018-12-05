from tinydb import TinyDB, Query

def sing(user_id, input):
    db = TinyDB('./db/db.json')
    user_db = db.table('user')

    User = Query()
    user = user_db.get(User.id == user_id)
    numerator = 1
    if user:
        if user['sing_num']:
            numerator = user['sing_num'] + 1
    else:
        user_db.insert({ 'id': user_id })
    
    user_db.update({ 'sing_num': numerator }, User.id == user_id)
    return db.table('sing').get(Query().numerator == numerator)['lyric']