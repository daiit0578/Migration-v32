import requests
data = '''{"images": "{\"ci\": {\"type\": \"download\", \"path\": \"2020/12/BSNISYNT5.04BANAPWl.png\", \"params\": {\"url\": \"http://localhost/wordpress/images/BSNISYNT5.04BANAPW-l.png\", \"rename\": true}}}"}'''
a = requests.post('http://192.168.42.106/wordpress/le_connector/connector.php?&encode=no&action=image&token=200f90ecc40048f9b967fd815154110b&cart_type=woocommerce&time=1608797039', data = data)
b = 1
print(a.status_code)
print(a.content)