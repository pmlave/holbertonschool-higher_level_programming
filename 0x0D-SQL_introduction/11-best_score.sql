-- Listing records that match certain tags and only when tag score is >= 10
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
