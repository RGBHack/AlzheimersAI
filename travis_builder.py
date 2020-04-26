import gdown

url = 'https://drive.google.com/uc?export=download&confirm=hUDJ&id=13p1H157cPDB8aBE_fZQd5kZgIHvI7XS9'
output = './server/src/pkl_file/export.pkl'
md5 = 'ba45410a87940fab98dad951056d5f8d'

gdown.cached_download(url, output, md5=md5)