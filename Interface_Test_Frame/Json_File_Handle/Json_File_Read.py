#coding = utf-8
import json,os

class json_file_read(object):
    def __init__(self):
        super().__init__()
        
        
    def read_contents_from_json(self,json_file_name):
        if not json_file_name:
            return None
        try:
            with open('./Json_File_Handle/%s.json'%json_file_name,'r',encoding='utf-8') as open_json:
                return json.load(open_json)
        except Exception as e:
            return None

        
        
    def read_content_from_json(self,case_id,json_file_type):
        if not json_file_type:
            return None
        try:
            with open('./Json_File_Handle/%s.json'%json_file_type,'r',encoding='utf-8') as open_json:
                json_file_content = json.load(open_json)
            if json_file_content:
                for header_data  in json_file_content[json_file_type]:
                    if list(header_data.keys())[0] == case_id:
                        return header_data[case_id]
            return None
        except Exception as e:
            print(e)
            return None
    
    
    def send_request_result_data_to_json(self,case_id,result_data):
        try:
            with open('./Json_File_Handle/%s.json'%case_id,'w') as open_json:
                json.dump({case_id:json.loads(result_data)},open_json)
        except Exception as e:
            print(e)
        
    
    
