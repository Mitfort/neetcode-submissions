-- Write your query below
-- SELECT r.student_id, r.exam_id
-- FROM 
--     (
--         SELECT e.student_id, e.exam_id, e.score
--         FROM exam_results e
--         WHERE e.score = (SELECT MAX(e2.score) FROM exam_results e2 GROUP BY e2.student_id LIMIT 1)
--     ) r 

SELECT r.student_id, r.exam_id, r.score
FROM exam_results r
WHERE r.score = (SELECT MAX(e.score) FROM exam_results e WHERE r.student_id = e.student_id)
AND r.exam_id = (SELECT MIN(e.exam_id) FROM exam_results e WHERE r.score = e.score AND r.student_id = e.student_id)
ORDER BY r.student_id ASC;