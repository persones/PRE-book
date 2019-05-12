# -*- coding: utf-8 -*-
import plivo

client = plivo.RestClient(auth_id='MANDFIOWUXZWZJYWZLZM', auth_token='NmFkNTQ0MTliN2VjYzcyMDkzOTdmMzdlZWVmNzA1')
response = client.messages.create(
    src='16173406483',
    dst='16173863368',
    text='Test Message', )
print(response)