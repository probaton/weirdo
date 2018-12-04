from tinydb import TinyDB

db = TinyDB('./db/db.json')
db.purge_table('sing')
sing_db = db.table('sing')

lyrics = [ 
    "When you were here before",
    "Couldn't look you in the eye",
    "You're just like an angel",
    "Your skin makes me cry",
    "You float like a feather",
    "In a beautiful world",
    "And I wish I was special",
    "You're so fuckin' special",
    "But I'm a creep, I'm a weirdo.",
    "What the hell am I doing here?",
    "I don't belong here.",
    "I don't care if it hurts",
    "I want to have control",
    "I want a perfect body",
    "I want a perfect soul",
    "I want you to notice",
    "When I'm not around",
    "You're so fuckin' special",
    "I wish I was special",
    "But I'm a creep, I'm a weirdo.",
    "What the hell am I doing here?",
    "I don't belong here.",
    "She's running out again,",
    "She's running out",
    "She's run run run run",
    "Whatever makes you happy",
    "Whatever you want",
    "You're so fuckin' special",
    "I wish I was special",
    "But I'm a creep, I'm a weirdo,",
    "What the hell am I doing here?",
    "I don't belong here.",
    "I don't belong here.",
]

lyric_array = []
count = 1
for l in lyrics:
    lyric_array.append({ 'numerator': count, 'lyric': l })
    count += 1
sing_db.insert_multiple(lyric_array)
    