from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def create_and_return_example(tx, code, test_data):
        query = """
            CREATE(n:TEST{
                description: $test_data,
                code: $code
            })
        """
        result = tx.run(
            query, 
            test_data = test_data,
            code = code
        )

        try:
            return [{"test_data": row["n"]["description"]} for row in result]

        # Capture any errors along with the query and data for traceability

        except ServiceUnavailable as exception:

            print("{query} raised an error: \n {exception}".format(query=query, exception=exception))

            raise

def get_amount_data(tx):
    query = """
        MATCH(n) RETURN COUNT(n) AS amount;
    """
    try:
        result = tx.run(query)
        return [{
            'amount':row['amount']
        } for row in result]

    except ServiceUnavailable as exception:

        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))

        raise

uri = "bolt://localhost:7687"
user = "neo4j"
password = ""

driver = GraphDatabase.driver(uri, auth=(user, password))

code = 2
teste_data = "Createing a new node..."

with driver.session() as session:
    session.execute_write(create_and_return_example, code, teste_data)

with driver.session() as session:
    result = session.execute_read(get_amount_data)
    print(result[0]['amount'])
driver.close()