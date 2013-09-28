-- keywords ordered by number of organic results in the top 75 list
SELECT COUNT(*),kw.keyword FROM organic_map om JOIN url ON om.url_id=url.id JOIN keyword kw ON keyword_id=kw.id WHERE domain_id NOT IN (
  SELECT domain_id FROM url GROUP BY domain_id ORDER BY COUNT(*) desc LIMIT 75) GROUP BY kw.keyword ORDER BY COUNT(*) DESC;

--- keywords ordered by site rank, higher average rank are shittier sites getting traffic for those keywords
SELECT AVG(rank), SUM(rank), keyword FROM keyword kw 
JOIN organic_map om ON kw.id=om.keyword_id JOIN url ON om.url_id=url.id JOIN domain d ON url.domain_id=d.id JOIN domain_traffic dt ON dt.id=d.id GROUP BY keyword ORDER BY AVG(rank) DESC;
