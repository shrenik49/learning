
SELECT_ALL_CONTACTS = '''
    SELECT * FROM contacts
'''

SELECT_CONTACT_BY_NAME = '''
    SELECT * FROM contacts WHERE name = ?
'''

SELECT_CONTACT_BY_NUMBER = '''
    SELECT * FROM contacts WHERE phone_number = ?
'''

INSERT_INTO_TABLE = '''INSERT INTO contacts(
            name, phone_number) VALUES 
            (?,?)'''

UPDATE_TABLE = '''UPDATE contacts set phone_number = (?) where name=(?)'''
DELETE_FROM_TABLE = '''DELETE FROM contacts where name = (?)'''