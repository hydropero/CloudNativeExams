def lambda_handler(event, context):
    """
    This function creates a new RDS database table and writes records to it
    """
    import sys
    import json
    import psycopg2
    from enum import Enum
    # rds settings
    rds_host  = "examdb.cbjixjfmxmrh.us-east-1.rds.amazonaws.com"
    user_name = "postgres"
    password = "Pro891630!"
    db_name = "postgres"
    scores_json = json.loads(event['body'])
    print(f"this is scores_json {scores_json}")
    username = scores_json['username']
    shortname = scores_json['shortname']
    score = scores_json['score']
    time_elapsed = scores_json['time_elapsed']
    exam_number = scores_json['exam_number']
    class Columns(Enum):
        C1 = "userid"
        C2 = "shortname"
        C3 = "score"
        C4 = "time_elapsed"
        C5 = "exam_number"

    # create the database connection outside of the handler to allow connections to be
    # re-used by subsequent function invocations.
    try:
        conn = psycopg2.connect(f"dbname={db_name} user={user_name} password={password} host={rds_host}")
        cur = conn.cursor()
    except Exception as e:
        print(e)
        sys.exit()
    try:
        print(event)
        cur.execute(f"INSERT INTO examscores ({Columns.C1.value}, {Columns.C2.value}, {Columns.C3.value}, {Columns.C4.value}, {Columns.C5.value}) VALUES(%s, %s, %s, %s, %s)", (username, shortname, score, time_elapsed, exam_number))
        conn.commit()
    except Exception as e:
        print(e)
        sys.exit()
    print('Successfully connected to DB')
    return event
    # message = event['Records'][0]['body']
    # data = json.loads(message)
    # CustID = data['CustID']
    # Name = data['Name']

    # item_count = 0
    # sql_string = f"insert into Customer (CustID, Name) values({CustID}, '{Name}')"

    # with conn.cursor() as cur:
    #     cur.execute("create table if not exists Customer ( CustID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (CustID))")
    #     cur.execute(sql_string)
    #     conn.commit()
    #     cur.execute("select * from Customer")
    #     logger.info("The following items have been added to the database:")
    #     for row in cur:
    #         item_count += 1
    #         logger.info(row)
    # conn.commit()

    # return "Added %d items to RDS MySQL table" %(item_count)
    
