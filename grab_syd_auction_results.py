from lxml import html
import requests

def get_value_without_key(generated_list):
	return generated_list[0].split(" ")[0]

# Currently, updated weekly - ending on the Sunday
page = requests.get('https://www.realestate.com.au/auction-results/nsw')
tree = html.fromstring(page.content)

# Create list from raw XPath query
date = tree.xpath('/html/body/section/section[1]/p/time/@datetime')
clearance_rate_percentage = tree.xpath('/html/body/main/section[1]/div[3]/div[1]/span[1]/text()')
total_sched_auctions = tree.xpath('/html/body/main/section[1]/div[1]/div[1]/text()')
sold_prior_to_auction = tree.xpath('/html/body/main/section[1]/ul/li[1]/text()')
passed_in = tree.xpath('/html/body/main/section[1]/ul/li[5]/text()')
sold_at_auction = tree.xpath('/html/body/main/section[1]/ul/li[2]/text()')
withdrawn = tree.xpath('/html/body/main/section[1]/ul/li[4]/text()')
sold_after_auction = tree.xpath('/html/body/main/section[1]/ul/li[3]/text()')

date_value = date[0]
clearance_rate_percentage_value = str(clearance_rate_percentage[0]).replace('%', '')
total_sched_auctions_value = total_sched_auctions[0]
sold_prior_to_auction_value = get_value_without_key(sold_prior_to_auction)
passed_in_value = get_value_without_key(passed_in)
sold_at_auction_value = get_value_without_key(sold_at_auction)
withdrawn_value = get_value_without_key(withdrawn)
sold_after_auction_value = get_value_without_key(sold_after_auction)

f = open('syd_results.csv', 'ab')
comma = ','
# TODO: Check this weeks results with last weeks for dupe
results_this_week = (date_value, clearance_rate_percentage_value, total_sched_auctions_value,
					 sold_prior_to_auction_value, passed_in_value, sold_at_auction_value,
					 withdrawn_value, sold_after_auction_value)
f.write(comma.join(results_this_week) + '\n')
f.close()
