-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- lists all rows of a database that have one column in common
SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows_genres
JOIN tv_shows ON tv_shows_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
