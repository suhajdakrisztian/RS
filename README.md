**RS Reddit Scraper**  
Reddit scraper for monitoring r/wallsreetbets and filtering out the mentioned stock tickers.

**Limitations:**  
The software currently may indicate false positives as it does not considers the context of words/phrases. "Buy TSLA at $800" will return ["TSLA", "AT"] because AT is the ticker of AT&T.

**TODO:**  
Fix false poistives by applying NLP on the extracted headlines.  

*Written on Ubuntu 20.04 under WSL*
