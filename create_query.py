import numpy as np
def create_query(services, data,status, time):
    data = {
        "services": {
            "camera":services[0],
            "NLP":services[1],
            "move":services[2]
        },
        "data": {
            "image": data[0],
            "audio": data[1],
            "movement":{
              "category":"d_drive",
              "errors":{
                "error": 3,
                "e_old": 0,
                "e_sum": 0
              } 
            }
        },
        "status": status, # -1 for not possible, 0 for unoccupied, 1 for occupied and 2 for done 
        "time":time
    }
    return data 
