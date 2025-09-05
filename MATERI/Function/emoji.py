def novert_mood(list_mood):
    mood_list = {
        "senang": "(❁´◡`❁)",
        "kangenn": "(づ￣ 3￣)づ",
        "turu ieu": "(∪.∪ )...zzz",
        "apaan sih" : "(▀̿Ĺ̯▀̿ ̿)"
    }

    return list(map(lambda m: mood_list.get(m, "🧠"),list_mood))
