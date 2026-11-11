# Write your MySQL query statement below
(SELECT u.name AS results
FROM Users u
JOIN MovieRating r ON u.user_id = r.user_id
GROUP BY u.user_id, u.name
ORDER BY COUNT(r.movie_id) DESC, u.name ASC
LIMIT 1)

UNION ALL

(SELECT m.title AS results
FROM Movies m
JOIN MovieRating r ON m.movie_id = r.movie_id
WHERE r.created_at LIKE '2020-02%'
GROUP BY m.movie_id, m.title
ORDER BY AVG(r.rating) DESC, m.title ASC
LIMIT 1);