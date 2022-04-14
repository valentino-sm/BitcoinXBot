import os

from loguru import logger


class SSL:
    # openssl req -newkey rsa:2048 -sha256 -nodes -x509 -days 365 \
    # -keyout cert.key \
    # -out cert.crt \
    # -subj "/C=RU/ST=Saint-Petersburg/L=Saint-Petersburg/O=Example Inc/CN=[IP_ADDRESS]"
    cert = "cert.crt"
    pkey = "cert.key"
    try:
        with open(os.path.join(os.getcwd(), cert), 'rb') as cert_file:
            cert_file = cert_file.read()
            # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            # ssl_context.load_cert_chain(cert, pkey)
            enable = True
    except Exception as e:
        logger.warning(e)
        enable = False


ssl = SSL()
