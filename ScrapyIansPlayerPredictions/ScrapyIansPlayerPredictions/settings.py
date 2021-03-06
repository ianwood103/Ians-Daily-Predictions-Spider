BOT_NAME = 'ScrapyIansPlayerPredictions'

SPIDER_MODULES = ['ScrapyIansPlayerPredictions.spiders']
NEWSPIDER_MODULE = 'ScrapyIansPlayerPredictions.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Sets up Splash with Scrapy
SPLASH_URL = 'http://0.0.0.0:8050/'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
