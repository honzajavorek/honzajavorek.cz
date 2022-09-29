import sys
from operator import attrgetter
from multiprocessing import Pool
from pathlib import Path

import feedparser
import requests
from pod2gen import Episode, Media, Person, Podcast
from yt_dlp import YoutubeDL


EPISODES_DIR = Path('.dvtv')

PODCAST_FILE = EPISODES_DIR / 'podcast.xml'

ARCHIVE_FILE = EPISODES_DIR / 'download-archive.txt'


def process_entry(entry):
    audio_file = EPISODES_DIR / f'{entry.id}.m4a'
    options = {
        'outtmpl': str(audio_file),
        'download_archive': ARCHIVE_FILE,
        'noplaylist': True,
        'format': audio_file.suffix.lstrip('.'),
    }
    try:
        with YoutubeDL(options) as yt_dlp:
            yt_dlp.download([entry.link])
    except Exception as e:
        print(f'{e} - {entry.link}', file=sys.stderr)
        return None

    return Episode(id=entry.id,
                   title=entry.title,
                   publication_date=entry.published,
                   link=entry.link,
                   summary=entry.summary,
                   media=Media(f"https://honzajavorek.cz/dvtv/{audio_file.name}",
                               size=audio_file.stat().st_size,
                               type='audio/m4a'))


if __name__ == '__main__':
    response = requests.get('https://video.aktualne.cz/rss/dvtv/')
    response.raise_for_status()
    rss = feedparser.parse(response.content)
    podcast = Podcast(name='Neoficiální DVTV podcast',
                      description='DVTV videa ve formě podcastu, pro osobní potřebu Honzy Javorka.',
                      language='cs',
                      website='https://video.aktualne.cz/dvtv/',
                      feed_url='https://junior.guru/api/podcast.xml',
                      authors=[Person('Aktuálně.cz')],
                      web_master=Person('Honza Javorek', 'mail@honzajavorek.cz'),
                      generator='honzajavorek.cz (+https://github.com/honzajavorek/honzajavorek.cz)',
                      image='https://www.dvtv.cz/static/img/favicon.png',
                      explicit=False)

    entries = sorted(rss.entries, key=attrgetter('published'), reverse=True)
    EPISODES_DIR.mkdir(exist_ok=True)
    with Pool() as pool:
        for episode in filter(None, pool.imap_unordered(process_entry, entries)):
            podcast.add_episode(episode)
    podcast.rss_file(str(PODCAST_FILE))
