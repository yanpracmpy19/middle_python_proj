BEGIN;
--
-- Create model Filmwork
--
CREATE TABLE "content"."film_work" ("id" uuid NOT NULL PRIMARY KEY, "title" varchar(255) NOT NULL, "description" text NOT NULL, "creation_date" date NOT NULL, "rating" double precision NOT NULL, "type" varchar(10) NOT NULL, "created" timestamp with time zone NOT NULL, "modified" timestamp with time zone NOT NULL);
--
-- Create model Genre
--
CREATE TABLE "content"."genre" ("id" uuid NOT NULL PRIMARY KEY, "name" varchar(255) NOT NULL, "description" text NOT NULL, "created" timestamp with time zone NOT NULL, "modified" timestamp with time zone NOT NULL);
COMMIT;
