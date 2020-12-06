import scrapy 


class WebSpider(scrapy.Spider):
    name = 'activities'
    start_urls = [
        'http://capetown.travel/events/'
    ]
    
    custom_settings = {'FEED_EXPORT_ENCODING': 'utf-8'} 
    
    def parse(self,response):
        all_div_activities = response.css('div[class*=tribe-events-content]')
        
        
        for a in all_div_activities:
            
            title = a.css("h2[class*='tribe-events-list-event-title'] > a::text").extract()
            
            
            if a.css("span.ticket-cost::text"):
                price = a.css('span.ticket-cost::text').get()
                
                
            else: 
                price = "No price"
                
                
            details = a.css("div[class*='tribe-events-list-event-description'] > p::text").get()
            
        
            yield { 
                'title':title.strip(),
                'price':price,
                'details':details
           } 
        