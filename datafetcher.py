import requests
import polars as pl
import duckdb as ddb
import io
import csv
from dfspecificfunc import *


def csvquery(source, url, key):
    try:
        urltxt = url
        r = requests.get(urltxt)
        reader = csv.reader(io.StringIO(r.text))
        rowls = [row for row in reader]
        headers = rowls[0]
        rowls = rowls[1:]
        
        df = pl.DataFrame(rowls, schema = headers, orient = "row")
        return df
    except :
        print(
            "Invalid URL"
        )




def databasepopulator(path):
        sources = pl.read_csv("data_ref/url.csv")
        sourcesdict = sources.to_dicts()
        for s in sourcesdict:
            res = csvquery(s['source'], s['url'], s['key'])
            if s['source'] == 'REPD':
                res = repd_proc(res)
                # Read only to false to allow me to write to the new db.
                with ddb.connect(database = path, read_only = False) as con:
                     con.execute(f"CREATE TABLE IF NOT EXISTS {s['source']} AS SELECT * FROM res;")

