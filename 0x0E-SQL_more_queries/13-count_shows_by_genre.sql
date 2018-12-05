-- List the count of shows that fall into all of the genre categories
SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres, tv_show_genres WHERE tv_genres.id=tv_show_genres.genre_id
GROUP BY name, genre_id HAVING (COUNT(genre_id)>0)
ORDER BY number_of_shows DESC;
