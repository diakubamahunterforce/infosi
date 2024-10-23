import  json
import  pathlib
class  json_read_file():
    @classmethod
    def   read_json(cls,):

        json_path=pathlib.Path('listurls_bank_angola.json').read_text()

        return   json.loads(json_path)

    def read_json1(cls, file):

        json_path = pathlib.Path(file).read_text()

        return json.loads(json_path)

#print(json_read_file.read_json())