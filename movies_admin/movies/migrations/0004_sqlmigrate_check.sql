BEGIN;
--
-- Alter unique_together for personfilmwork (1 constraint(s))
--
ALTER TABLE "content"."person_film_work" ADD CONSTRAINT "person_film_work_film_work_id_person_id_743d4e91_uniq" UNIQUE ("film_work_id", "person_id");
COMMIT;
