-- Select the title of the TV show and the genre_id (which will be NULL if there is no genre linked)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- Perform a LEFT JOIN to include all TV shows and link to genres, if they exist
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Filter the results to include only those TV shows that do not have any linked genres
WHERE tv_show_genres.genre_id IS NULL
-- Sort the results by the title of the TV show
ORDER BY tv_shows.title, tv_show_genres.genre_id;

