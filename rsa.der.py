from cryptography import x509

f = open('2048b-rsa-example-cert.der', 'rb')
cert = x509.load_der_x509_certificate(f.read())

modulus = cert.public_key().public_numbers().n
public_exponent = cert.public_key().public_numbers().e

print(modulus)
    