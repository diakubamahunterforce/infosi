import  json
import  pathlib
class  json_read_file():
    @classmethod
    def   read_json(cls):

        json_path=pathlib.Path('listurls_bank_angola.json').read_text()

        return   json.loads(json_path)



