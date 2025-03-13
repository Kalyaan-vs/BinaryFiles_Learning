import hashlib

published_hash = "4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"

file_name = "colorama-0.4.6-py2.py3-none-any.whl"

with open(file_name, "rb" ) as downloaded_file:
    content = downloaded_file.read()

file_hash = hashlib.sha256(content).hexdigest()
print(file_hash)

if published_hash == file_hash:
    print(f"The file {file_name} hash is correct")
else:
    print(f"The file {file_name} hash is correct")