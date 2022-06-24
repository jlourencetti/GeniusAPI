import boto3
import uuid


class DynamoDB:

    def __init__(self):
        
        self.ACCESS_KEY = "Cole aqui seu ACCESS_KEY"
        self.KEY_ID = 'Cole aqui seu KEY_ID'
        self.REGION = 'us-west-2'
        self.dynamodb = boto3.resource(service_name='dynamodb',
                                       region_name=self.REGION,
                                       aws_access_key_id=self.KEY_ID,
                                       aws_secret_access_key=self.ACCESS_KEY)
        self.key = str(uuid.uuid4())

    def create_table_artists(self):

        tables = list(self.dynamodb.tables.all())
        tables_name = [table.name for table in tables]

        if 'Artists' not in tables_name:
            
            table = self.dynamodb.create_table(
                TableName='Artists',
                KeySchema=[
                    {
                        'AttributeName': '_uuid',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'name',
                        'KeyType': 'RANGE'
                    },
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': '_uuid',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'name',
                        'AttributeType': 'S'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            )
            return table

    
    def insert_artists_songs(self, artist_name, songs):
    
        table = self.dynamodb.Table('Artists')

        try:
            table.put_item(Item={'_uuid': self.key, 'name': artist_name, 'songs': songs})
            print('Registro inserido no DynamoDB com sucesso')
        except:
            print('Erro ao inserir registro na tabela')


if __name__ == '__main__':
    db = DynamoDB()
    db.create_table_artists()