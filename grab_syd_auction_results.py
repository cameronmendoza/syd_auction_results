from lxml import html
import requests

# Currently, updated weekly - ending on the Sunday
page = requests.get('https://www.realestate.com.au/auction-results/nsw')
tree = html.fromstring(page.content)

date = tree.xpath('/html/body/section/p/time/@datetime')
clearance_rate = tree.xpath('/html/body/main/section[1]/div[2]/div[1]/text()')
total_sched_auctions = tree.xpath('/html/body/main/section[1]/div[1]/div[1]/text()')
sold_prior_to_auction = tree.xpath('/html/body/main/section[1]/ul/li[1]/text()')
passed_in = tree.xpath('/html/body/main/section[1]/ul/li[2]/text()')
sold_at_auction = tree.xpath('/html/body/main/section[1]/ul/li[3]/text()')
withdrawn = tree.xpath('/html/body/main/section[1]/ul/li[4]/text()')
sold_after_auction = tree.xpath('/html/body/main/section[1]/ul/li[5]/text()')

# TODO: remove!
print date
print clearance_rate
print total_sched_auctions
print sold_prior_to_auction
print passed_in
print sold_at_auction
print withdrawn
print sold_after_auction

# sold_prior_to_auction_value = str(sold_prior_to_auction[0]).split('Sold prior to auction: ')
# print sold_prior_to_auction_value[1]
