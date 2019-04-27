import urllib.request,json
from .models import Quote



# Getting api key
api_key = None
# Getting the quotes base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['QUOTES_API_KEY']
    base_url = app.config['QUOTES_API_BASE_URL']

def get_quotes(category):
    '''
    Function that gets the json response to our url request
    '''
    get_quotess_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_movies_url) as url:
        get_quotess_data = url.read()
        get_quotess_response = json.loads(get_quotes_data)
        
        quotes_results = None
        
        if get_quotes_response['results']:
            quote_results_list = get_quotes_response['results']
            quotee_results = process_results(quote_results_list)
            
        return quote_results
        