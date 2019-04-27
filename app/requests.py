import urllib.request,json
from .models import Quote


#Quotes=quotes.Quotes
# Getting api key
api_key = None
# Getting the quotes base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['QUOTES_API_KEY']
    base_url = app.config['QUOTES_API_BASE_URL']

def get_quotes(quote):
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format(quote,api_key)
    
    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
        
        quotes_results = None
        
        if get_quotes_response['results']:
            quote_results_list = get_quotes_response['results']
            quote_results = process_results(quote_results_list)
            
        return quote_results
        
def process_results(quote_list):
    '''
    Function  that processes the quote result and transform them to a list of Objects

    Args:
        quote_list: A list of dictionaries that contain quote details

    Returns :
        quote_results: A list of quote objects
    '''
    quote_results = []
    for quote_item in quote_list:
        id = movie_item.get('id')
        author = quote_item.get('author')
        quote = quote_item.get('quote')
    

    return quote_results