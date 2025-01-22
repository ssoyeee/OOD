'''
As a backend engineer, 
how will you design your code such that it meets all the coding standards. 
(Easy to use and maintain, and clean code.)

Suppose you have an API that returns data. 
- you need to store it in multiple different types of databases. 
- The data can be of any type. 
- It can be a structured, unstructured, a text file, image, pdf, or even a video file. 

Strategy Pattern [Head First Design Pattern]
: defines a family of algorithms (methods regarding databases), encapsulates each one (using interface) , and make them interchangeable(). 
Strategy lets the algorithm vary independently from clients that use it.

ex) When building a game, we want to add a feature to 'a player' like below
    - can move
        - can walk
        - can run
        - (or we might wanna add) swim (in the future)
        - (we might wanna add) fly (in the future)
In this case, apply STRATEGY PATTERN, 
by separating the 'move' behavior from Player class, and encapsulating it in an interface
'''
from abc import ABC, abstractmethod

# Step 1: Define an interface for database operations
# Then, create separate classes for each type of storage, implementing the defined interface
class Datastore(ABC):
    @abstractmethod
    def initiate_connection(self) -> bool:
        """Initiate connection to the datastore."""
        pass

    @abstractmethod
    def insert_data(self, data: dict) -> dict:
        """Insert data into the datastore."""
        pass


# Implementations for specific datastores
class MySQL(Datastore):
    def initiate_connection(self) -> bool:
        print("Connecting to MySQL database...")
        return True

    def insert_data(self, data: dict) -> dict:
        print(f"Inserting data into MySQL: {data}")
        return {"status": "success", "db": "MySQL"}


class Cassandra(Datastore):
    def initiate_connection(self) -> bool:
        print("Connecting to Cassandra database...")
        return True

    def insert_data(self, data: dict) -> dict:
        print(f"Inserting data into Cassandra: {data}")
        return {"status": "success", "db": "Cassandra"}


class HDFS(Datastore):
    def initiate_connection(self) -> bool:
        print("Connecting to HDFS storage...")
        return True

    def insert_data(self, data: dict) -> dict:
        print(f"Inserting data into HDFS: {data}")
        return {"status": "success", "storage": "HDFS"}

# Step 2: Apply Strategy pattern 
# Define the Client class to manage datastore, which inserts data into the appropriate/respective datastore.

class Client:
    def __init__(self, storage_type: str):
        """
        # Initialize the appropriate datastore based on the storage type.
        """
        datastore_mapping = {
            "MySQL": MySQL,
            "Cassandra": Cassandra,
            "HDFS": HDFS
        }
        if storage_type in datastore_mapping:
            self.datastore = datastore_mapping[storage_type]()
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")

    def insert_data(self, data: dict) -> dict:
        """
        Inserts data into the selected datastore if the connection is successful.
        """
        if self.datastore.initiate_connection():
            return self.datastore.insert_data(data)
        return {"status": "failure", "message": "Connection failed"}


# Step 3: Simulate an API call and use the client to insert data
def get_data() -> dict:
    """
    Mock function to simulate an API call returning data.
    """
    return {"key": "value"}


# Main logic
if __name__ == "__main__":
    # Get data from the simulated API
    data = get_data()
    
    # Create a client for MySQL and insert the data
    client = Client("MySQL")
    response = client.insert_data(data)
    print(response)