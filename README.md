#how to run
## Run it as a desktop app 
```
pip install -r requirements.txt
python desktop_app.py
```

campaign_project/
├── generate_data.py       
├── analyze_campaigns.py   
├── campaign_data.csv      
├── campaign_metrics.csv   
├── channel_summary.csv    
└── README.md              

Column	Type	Meaning
campaign_id	text	unique ID per campaign
channel	text	Instagram, YouTube, Google Ads, Facebook Ads, Email, Referral
campaign_type	text	Brand Awareness, Lead Gen, Retargeting, Product Launch
date	date	campaign date
spend	number	ad spend
impressions	number	raw impressions
clicks	number	raw clicks
leads	number	raw leads
customers_acquired	number	paying customers from this campaign
revenue	number	revenue attributed to the campaign
CTR	number	clicks / impressions
lead_conv_rate	number	leads / clicks
customer_conv_rate	number	customers_acquired / leads
CAC	number	spend / customers_acquired
ROI	number	(revenue − spend) / spend
ROAS	number	revenue / spend
month	text	YYYY-MM, for time grouping