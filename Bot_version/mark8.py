# Import sqlite3
import sqlite3
import rasa_nlu
# Open connection to DB
conn = sqlite3.connect('/ChatBot/hotels.db')

# Create a cursor
c = conn.cursor()

# Define area and price
area, price = "south", "hi"
t = (area, price)

# Execute the query
c.execute('SELECT * FROM hotels WHERE area=? AND price=?', t)

# Print the results
print(c.fetchall())

# Define find_hotels()
def find_hotels(params):
    # Create the base query
    query = 'SELECT * FROM hotels'
    # Add filter clauses for each of the parameters
    if len(params) > 0:
        filters = ["{}=?".format(k) for k in params]
        query += " WHERE " + " and ".join(filters)
    # Create the tuple of values
    t = tuple(params.values())
    
    # Open connection to DB
    conn = sqlite3.connect('hotels.db')
    # Create a cursor
    c = conn.cursor()
    # Execute the query
    c.execute(query, t)
    # Return the results
    return c.fetchall()

# Create the dictionary of column names and values
params = {"area":"south" , "price" :"lo"}
# Find the hotels that match the parameters
print(find_hotels(params))

# Define respond()
def respond(message):
    # Extract the entities
    entities = interpreter.parse(message)["entities"]
    # Initialize an empty params dictionary
    params = {}
    # Fill the dictionary with entities
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])

    # Find hotels that match the dictionary
    results = find_hotels(params)
    # Get the names of the hotels and index of the response
    names = [r[0] for r in results]
    n = min(len(results),3)
    # Select the nth element of the responses array
    return responses[n].format(*names)
    
print(respond("I want an expensive hotel in the south of town")) 



