BEGIN;
--
-- Add field certificate to filmwork
--
ALTER TABLE "content"."film_work" ADD COLUMN "certificate" varchar(512) DEFAULT '' NOT NULL;
ALTER TABLE "content"."film_work" ALTER COLUMN "certificate" DROP DEFAULT;
--
-- Add field file_path to filmwork
--
ALTER TABLE "content"."film_work" ADD COLUMN "file_path" varchar(100) NULL;
COMMIT;
