USE artobject;
-- Q1
SHOW TABLES;
SHOW TRIGGERS;
/* The triggers listed here are ones created in this query, however, the database initialization script
contains other triggers ON DELETE and ON UPDATE which modify the tuples based on whether SET NULL or 
CASCADE, follows these two key phrases. On SET NULL, if the tuple from the parent table containing a 
foreign key for a tuple in the child table is deleted, the attribute in the child tuple will be set to
null. If CASCADE, this tuple is deleted or updated with the modified information from the parent tuple.
An example of this is the Exhibit_name (FK) column from ART_OBJECT. ON DELETE of Exhibit_name from 
the parent tuple (EXHIBITION), this field will be set to null as the object no longer belongs to an existing
exhibition. However, the tuple itself isn't deleted as the object is still needed as part of the database.
For ON UPDATE, it is set to CASCADE as the new name is still relevant to the object.*/

SELECT 	CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE
FROM 	INFORMATION_SCHEMA.TABLE_CONSTRAINTS 
WHERE 	(CONSTRAINT_TYPE = 'FOREIGN KEY' OR CONSTRAINT_TYPE = 'PRIMARY KEY') AND CONSTRAINT_SCHEMA = 'artobject';
/*Foreign key constraints are useful as they enforce referential integrity. Therefore it is used to
ensure all foreign keys reference a value in the parent table. Primary key constraints ensure that 
each key used to identify a tuple is unique. For example, in ART_OBJECT, Id_no is a unique identifier
for each tuple, thereby being the primary key for the table. Id_no is also the foreign key for many
other tables in the schema. In these tables, the filled tuples must have a foreign key that is already
included in the parent table (ART_OBJECT).*/

-- Q2: All artists active during the Renaissance
SELECT	Artist_name
FROM	ARTIST
WHERE	Epoch = 'Renaissance';

-- Q3: Exhibitions in order of (most recent to oldest) start date
SELECT		Exhibit_name, Start_date, End_date
FROM		EXHIBITION
ORDER BY	Start_date DESC;

-- Q4: All art objects 'On loan'
SELECT	DISTINCT Id_no, Title, Art_desc
FROM	ART_OBJECT
WHERE	Id_no IN 	(SELECT	Id_no
					FROM	PERMANENT_COLLECTION
					WHERE	Pcoll_status = 'On loan');

-- Q5: Retrieve all sculptures by Picasso that use painted wood
SELECT	ART_OBJECT.Id_no, Title, Year_made, Material, Style, Art_desc
FROM	SCULPTURE_OR_STATUE JOIN ART_OBJECT ON SCULPTURE_OR_STATUE.Id_no = ART_OBJECT.Id_no
WHERE	Artist_name = 'Pablo Picasso' AND Material LIKE '%painted wood%';

-- Q6: UPDATES all art_object with Baroque Epoche to be included in 
-- 'The Rediscovery of The Baroque Period' Exhibition.
-- TRIGGER checks to ensure that art_object in Exhibitions that have dates that overlap
-- 'The Rediscovery of The Baroque Period' Exhibition date are not moved.

SELECT	Id_no, Title, Exhibit_name -- original relevant table
FROM 	ART_OBJECT;

DROP TRIGGER IF EXISTS DISPLAYED_EXHIBIT_UPDATE_VIOLATION;
CREATE TRIGGER DISPLAYED_EXHIBIT_UPDATE_VIOLATION
BEFORE UPDATE ON ART_OBJECT
FOR EACH ROW
	SET NEW.Exhibit_name = IF(	(((SELECT DISTINCT End_date
										FROM	EXHIBITION
                                        WHERE	NEW.Exhibit_name = Exhibit_name) > 
                                        (SELECT	DISTINCT Start_date 
                                        FROM	EXHIBITION
										WHERE	OLD.Exhibit_name = Exhibit_name))
                                        AND
                                        ((SELECT	DISTINCT Start_date
                                        FROM	EXHIBITION
                                        WHERE	NEW.Exhibit_name = Exhibit_name) <
                                        (SELECT	DISTINCT End_date 
                                        FROM	EXHIBITION
										WHERE	OLD.Exhibit_name = Exhibit_name))),
								OLD.Exhibit_name,
                                NEW.Exhibit_name);

UPDATE	ART_OBJECT
SET		Exhibit_name = 'The Rediscovery of The Baroque Period'
WHERE	Epoch = 'Baroque';

SELECT	Id_no, Title, Exhibit_name -- shows successful update of art_objects' move to 'Baroque' exhibit
FROM 	ART_OBJECT;

-- Q7: Delete artist tuple from database if not needed anymore
SELECT	Artist_name, Artist_desc -- shows original relevant tables
FROM ARTIST
ORDER BY Artist_name;
SELECT	Id_no, Title, Artist_name
FROM ART_OBJECT
ORDER BY Artist_name;

DROP TRIGGER IF EXISTS ARTIST_NOT_NEEDED;
CREATE TRIGGER ARTIST_NOT_NEEDED
BEFORE DELETE ON ART_OBJECT
FOR EACH ROW
	DELETE FROM	ARTIST
    WHERE Artist_name IN 	(SELECT		Artist_name
							FROM		ART_OBJECT
                            WHERE		ART_OBJECT.Id_no = OLD.Id_no
                            GROUP BY	Artist_name
                            HAVING		COUNT(Artist_name) = 1);

DELETE FROM	ART_OBJECT
WHERE		Id_no = 'AO_0021' OR Id_no = 'AO_0022';

SELECT	Artist_name, Artist_desc -- Shows that vincent van gogh was deleted from ARTIST
FROM ARTIST
ORDER BY Artist_name;
SELECT	Id_no, Title, Artist_name -- Confirms selected art_objects were deleted
FROM ART_OBJECT
ORDER BY Artist_name;
