-- Q1
SHOW TABLES;
/*explain*/

-- Q2: All artists active during the Renaissance
SELECT	Artist_name
FROM	ARTIST
WHERE	Epoch = 'Renaissance';

-- Q3: Exhibitions in order of (most recent to oldest) start date
SELECT		Exhibit_name, Start_date, End_date
FROM		EXHIBITION
ORDER BY	Start_date DESC;

-- Q4: All art objects in 'The Tudors' exhibition
SELECT	DISTINCT ART_OBJECT.Id_no, Title, Art_desc
FROM	DISPLAYED_IN, ART_OBJECT
WHERE	ART_OBJECT.Id_no IN (SELECT	Id_no
							FROM	DISPLAYED_IN
							WHERE	DISPLAYED_IN.Exhibit_name = 'The Tudors: Art and Majesty in Renaissance England');

-- Q5: Retrieve all artworks by Picasso
SELECT	ART_OBJECT.Id_no, Title, Year_made, Style, Art_desc
FROM	((ARTIST JOIN CREATES ON ARTIST.Artist_name = CREATES.Artist_name) JOIN ART_OBJECT ON CREATES.Id_no = ART_OBJECT.Id_no)
WHERE	ARTIST.Artist_name = 'Pablo Picasso';

-- Q6: UPDATES all art_object with Baroque Epoche to be included in 
-- 'The Rediscovery of The Baroque Period' Exhibition.
-- TRIGGER checks to ensure that art_object in Exhibitions that have dates that overlap
-- 'The Rediscovery of The Baroque Period' Exhibition date are not moved.

SELECT	*
FROM 	DISPLAYED_IN;

DROP TRIGGER IF EXISTS DISPLAYED_EXHIBIT_UPDATE_VIOLATION;
CREATE TRIGGER DISPLAYED_EXHIBIT_UPDATE_VIOLATION
BEFORE UPDATE ON DISPLAYED_IN
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

UPDATE	DISPLAYED_IN
SET		Exhibit_name = 'The Rediscovery of The Baroque Period'
WHERE	Id_no IN	(SELECT	Id_no
					FROM	ART_OBJECT
                    WHERE	Epoch = 'Baroque');

SELECT	*
FROM 	DISPLAYED_IN;

-- Q7: Deleted Objects from BORROWED collection move to PERMANENT_COLLECTION
SELECT	*
FROM ARTIST
ORDER BY Artist_name;
SELECT	*
FROM CREATES
ORDER BY Id_no;

DROP TRIGGER IF EXISTS ARTIST_NOT_NEEDED;
CREATE TRIGGER ARTIST_NOT_NEEDED
BEFORE DELETE ON ART_OBJECT
FOR EACH ROW
	DELETE FROM	ARTIST
    WHERE Artist_name IN 	(SELECT		Artist_name
							FROM		(ART_OBJECT JOIN CREATES ON ART_OBJECT.Id_no = CREATES.Id_no)
                            WHERE		ART_OBJECT.Id_no = OLD.Id_no
                            GROUP BY	Artist_name
                            HAVING		COUNT(Artist_name) = 1);

DELETE FROM	ART_OBJECT
WHERE		Id_no = 'AO_0021' OR Id_no = 'AO_0022';

SELECT	*
FROM ARTIST
ORDER BY Artist_name;
SELECT	*
FROM CREATES
ORDER BY Id_no;