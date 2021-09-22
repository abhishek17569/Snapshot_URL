import requests
from url_parser import url_parser


def urlvoid_response(url):
    domain_name=url_parser(url)
    url_hit='https://www.urlvoid.com/scan/' + domain_name + '/'
    response = requests.get(url_hit)
    r_text=response.text
    return r_text

def urlvoid_url(url):
    domain_name=url_parser(url)
    url_hit='https://www.urlvoid.com/scan/' + domain_name + '/'
    return url_hit

# domain_name='lcloud-singin.com'
# print(urlvoid(domain_name))
