from cryptography.fernet import Fernet

token = Fernet('Ds6gZnrn8StcSgyeJxVxZrYem0U8dBAl44-aWE37RWI=')

text = token.decrypt('gAAAAABmxXnr_5gWCzfGERg_LS1OdJ8jSHGtX_wbeqK4exdBjdCsevbe1v1CsmGVNSxPRfa4kdWXiuHJN-mF1yHKxMwdYf50ow==')

print(text)