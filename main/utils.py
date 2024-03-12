from dateutil import parser
from main import app
@app.template_filter('strftime')
def _jinja_filter_datetime(date, format=None):
    date = parser.parse(date)
    native = date.replace(tzinfo=None)
    format = '%M %d %Y' 
    return native.strftime(format)

