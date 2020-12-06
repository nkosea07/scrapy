""" def parse(self, response):
        all_div_activities = response.css("div.tribe-events-content")#gdlr-core-pbf-column gdlr-core-column-60 gdlr-core-column-first
        title = all_div_activities.css("h2.tribe-events-list-event-title::text").extract()#gdlr-core-text-box-item-content
        price = all_div_activities.css(".span.ticket-cost::text").extract()
        details = all_div_activities.css(".p::text").extract()
        yield {
            'title':title,
            'price':price,
            'details':details
        } """
        