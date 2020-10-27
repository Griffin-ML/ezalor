import json
import time
from datetime import datetime
import pandas as pd
from pathlib import Path
from pyhive import presto
from requests.auth import HTTPBasicAuth


def queryPrestoToDataframe(query_statement):
    try:
        cursor = _createCursor()
        print("{:%H:%M:%S} Presto Query Started".format(datetime.now()))
        cursor.execute(query_statement)
        # Wait for query to finish
        sqlState = cursor.poll()
        while sqlState["stats"]["state"].lower() != "finished":
            time.sleep(5)
            sqlState = cursor.poll()
            if("progressPercentage" in sqlState["stats"]):
                print('Query progress', '{:.2f}%'.format(sqlState["stats"]["progressPercentage"]))
            else:
                print('Query progress', sqlState["stats"]["state"])
        print("{:%H:%M:%S} Presto query completed".format(datetime.now()))
        columnNameList = [columnDataList["name"] for columnDataList in sqlState["columns"]]
        df = pd.DataFrame(cursor.fetchall(), columns=columnNameList)
        print("{:%H:%M:%S} Converted to pandas".format(datetime.now()))
        return df
        
    except Exception as e:
        print('Error Message', e)
        return -1


def _createCursor():
    try:
        config_path = str(Path.home()) + ".ezalor/config.json"
        with open(config_path) as securityConfig:
            securityConfig = dict(json.load(securityConfig))
    except IOError:
        raise IOError("Config file does not appear to exist")
    return presto.connect(host = securityConfig["host"],
        requests_kwargs={"auth": HTTPBasicAuth(securityConfig["user"], securityConfig["password"])},
        username=securityConfig["user"],
        catalog=securityConfig["catalog"],
        port=securityConfig["port"],
        protocol=securityConfig["protocol"]).cursor()

