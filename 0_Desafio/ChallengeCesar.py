import json
import hashlib
import requests

## HTTP Get JSON
def get_json():
    req = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=tokenaqui")
    json_dict = req.json()
    return (json_dict)

## Decrypt
def decrypt(old_sentence, jump):

    decrypt_sentence = ""

    for char in old_sentence:
        if char.isalpha():
            ascii_baseline = ord("a")
            char_cypher = ord(char) - ascii_baseline
            mod_char = (char_cypher - jump) % 26
            real_char = mod_char + ascii_baseline

        else:
            real_char = ord(char)

        decrypt_sentence += chr(real_char)
    
    print (decrypt_sentence)
    return decrypt_sentence


## Write SHA1
def write_SHA1(sentence):
    gen_sha1 = hashlib.sha1((sentence).encode('utf-8')).hexdigest()
    return gen_sha1

## Submit Post BACK
def submit_post(url, json_object):
    file_submit = {'answer' : open(json_object, "rb")}
    req = requests.post(url, files = file_submit)
    print(req.status_code)


## Open JSON
def open_json(filename, mode):
    with open(filename, mode) as file:
        copy = file.read()
        dict_return = json.loads(copy)
        return dict_return

## JSON Save
def save_json(json_dict, filename):
    with open(filename, "w") as file:
        json.dump(json_dict, file)

if __name__ == "__main__":
    new_json = get_json()
    decrypt_sentence = decrypt(new_json["cifrado"] , new_json["numero_casas"])
    sha1 = write_SHA1(decrypt_sentence)

    new_json["decifrado"] = decrypt_sentence
    new_json["resumo_criptografico"] = sha1

    save_json(new_json, "answer.json")
    submit_post(
        "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=tokenaqui",
        "answer.json")

