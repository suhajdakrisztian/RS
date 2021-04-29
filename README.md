**RS Reddit Scraper**  
Reddit scraper for monitoring r/wallsreetbets and filtering out the mentioned stock tickers.

**Limitations:**  
The script may currently indicate false positives as it does not consider the context of words/phrases. "Buy TSLA at $800" will return ["TSLA", "AT"] as AT is the ticker of AT&T.

**TODO:**
Fix false positives by applying NLP/Contextual analysis on the extracted headlines.

*Written on Ubuntu 20.04 LTS under WSL*
