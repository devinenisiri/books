import sqlite3
from flask_restful import Resource, request


class Item(Resource):
    def get(self,name):
        item = self.find_by_name(name)
        if item:
            return(item)
        return {'message': ' item not found'}
        
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()
        if row:
            return {'items': {'name':row[0], 'price': row[1]}}
       

    def post(self,name):
        if self.find_by_name(name):
            return {'message': " an item with name '{}' already exists.".format(name)}

        data = request.get_json()
        item = {'name':name, 'price':data['price']}
        
        
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)" 
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

        return item

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?" 
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'item deleted'}

    def put(self, name):
        item = self.find_by_name(name)

        data = request.get_json()
        updated_item = {'name':name, 'price': data['price']}

        if item is None:
            try:
                self.insert(updated_item) 
            except:
                return {'message': "an error occured inserting the item."} 
         
        else:
            try:
                self.update(updated_item)
            except:
                return {'message': "an error occured updating the item."}

        return item

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?" 
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()




        
     