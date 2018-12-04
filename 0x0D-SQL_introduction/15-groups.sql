-- Lists the amount of times any score value appears in the table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
