from stockMarket.models import ShareModel

def scraper_example(a, b):
    return a + b

def get_feed():
    i=0

    for share in ShareModel.objects.all() :
        share.get_feed()
        i=i+1

    return "done {0} times".format(i)