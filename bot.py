import os, glob, time, shutil, datetime
from telethon.sync import TelegramClient, events
from config import api_hash, api_id, channel_id

with TelegramClient('anon', api_id, api_hash) as client:
    @client.on(events.NewMessage(pattern=r'\$rip http'))
    async def handler(event):
        getURL = event.raw_text.split()
        parseLink = getURL[1]
        if 'tidal' in parseLink or 'qobuz' in parseLink or 'deezer' in parseLink:
            getStatus = await event.respond(f"Downloading FLAC")
        else:
            getStatus = await event.respond(f"Wrong Service")
            return None
        os.system(f'rip url {parseLink}')
        tempDir = './Temp/'
        loop = 0
        flac_File = sorted(glob.glob(tempDir+'/*/*.flac', recursive=True), key=os.path.getmtime)
        cover_file = glob.glob(tempDir+'/*/*.jpg', recursive = True)
        try:
            await client.send_file('me', cover_file[0])
        except:
            pass
        while loop < len(flac_File):
            await client.send_file('me', flac_File[loop])
            loop += 1

        shutil.rmtree(tempDir)
        resultComplete = await event.respond(f"Done")
    client.run_until_disconnected()
