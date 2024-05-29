-- Select the genre name and the count of shows linked to each genre
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
-- Join the genres table with the tv_show_genres table to link genres with shows
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
-- Group the results by genre name to aggregate the count of linked shows
GROUP BY genres.name
-- Only include genres that have at least one show linked
HAVING number_of_shows > 0
-- Order the results in descending order by the number of shows linked to each genre
ORDER BY number_of_shows DESC;
