import requests   #importing libraries
  

downloadUrl = ' https://xkcd.com/{comic_id}/info.0.json'

#pseudo code
req = requests.get(downloadUrl)
filestar = req.url[downloadUrl.rfind('/')+1:]   #allocating a unique name as filestar

with open(filestar, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)              #pasting and writing the contents in file

def download_file(url, filename=''):
    try:
        if filestar:
            pass            
        else:
            filestar = req.url[downloadUrl.rfind('/')+1:]

        with requests.get(url) as req:
            with open(filestar, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filestar
    except Exception as e:
        print(e)
        return None


downloadLink = ' https://xkcd.com/{comic_id}/info.0.json'

download_file(downloadLink, 'documets')

