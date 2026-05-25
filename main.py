import os
import sys
import duckdb as ddb
from datafetcher import *

def main():
    print("Hello from solardataeng!")
    # Resolving directory based issues
    #1 . Check that data folder exists.
    cwd = os.path.dirname(os.path.abspath(sys.argv[0]))
    dirls = os.listdir(cwd)
    try:
        
        if 'data' in dirls:
            dbdir = os.path.join(cwd, "data")
            print("Data Directory located here: ", dbdir )
        else:
            dbpdir = os.path.join(cwd, "data")
            os.mkdir(dbdir)
    except Exception as e:
        print(f"Error {e}")
    #2 . Create the database (if it does not yet exist)
    dbloc = os.path.join(dbdir, 'solarprojects.db')
    try:
        con = ddb.connect(dbloc)
        con.close()
    except Exception as e:
        print(f"Error, {e}")
    #3 . Check for the url reference csv
    try:
        if 'data_REF' in dirls:
            urlpath = os.path.join(cwd, "data_REF")
            print("Ref URLs located here: ", urlpath)
        else:
            print("Need to locate where the reference data folder is located.")
            return None
    except Exception as e: 
        print(f"Error {e}")
    # 4. Run pipeline
    try:
        databasepopulator(dbloc)
        print("Tables built - Success!")
    except Exception as e:
        print(f"Populator script  due to {e}.")

if __name__ == "__main__":
    main()
    
    

