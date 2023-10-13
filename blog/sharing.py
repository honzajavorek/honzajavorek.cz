def prepare_text(article: dict) -> str:
    if 'týdenní poznámky' in article['tags']:
        text = f"Týdenní poznámky! Jak se mi daří v jednom člověku provozovat a rozvíjet junior.guru?"
    elif 'junior.guru' in article['tags']:
        text = f"„{article['title']}” Jak se mi daří v jednom člověku provozovat a rozvíjet junior.guru?"
    else:
        text = f"„{article['title']}”"

    readtime = article['readtime']
    if readtime < 5:
        emoji = "😎"
    elif readtime < 15:
        emoji = "🧐"
    elif readtime < 30:
        emoji = "😅"
    else:
        emoji = "🙈"
    return f"{text} Tentorkát je to na {article['readtime']} min čtení {emoji} {article['url']}"
