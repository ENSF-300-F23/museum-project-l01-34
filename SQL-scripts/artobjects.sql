DROP DATABASE IF EXISTS ARTOBJECT;
CREATE DATABASE ARTOBJECT; 
USE ARTOBJECT;

CREATE TABLE ARTIST
	(Artist_name		VARCHAR(40)		not null,
    Date_born			INTEGER			default null,
    Date_died			INTEGER			default null,
    Country_of_origin	VARCHAR(20),
    Main_style			VARCHAR(20),
    Epoch				VARCHAR(20),
    Artist_Desc			VARCHAR(60),
    CONSTRAINT ARTPK PRIMARY KEY (Artist_name));

INSERT INTO ARTIST (Artist_name, Date_born, Date_died, Country_of_origin, Main_style, Epoch, Artist_desc)
VALUES
('R W', '1560', '1615', 'United Kingdom', 'Renaissance', 'Renaissance', 'Unknown'), 
('Robert Peake the Elder', '1551', '1619', 'United Kingdom', 'Realism', 'Renaissance', 'An English painter during Queen Elizabeth I\’s reign.'), 
('Hans Holbein the Younger', '1497', '1543', 'Germany', 'Realism', 'Renaissance', 'A German-Swiss painter and printmaker.'), 
('Pietro Torrigiano', '1472', '1528', 'Italy', 'Realism', 'Renaissance', 'An Italian sculptor.'), 
('Donatello', '1386', '1466', 'Italy', 'Early Renaissance', 'Renaissance', 'Italian sculptor of the early Renaissance.'), 
('Andrea della Robbia', '1435', '1525', 'Italy', 'Romantic', 'Renaissance', 'An Italian artist.'), 
('Giambologna', '1529', '1608', 'Italy', 'Neoclassicism', 'Renaissance', 'An Italian artist.'), 
('Pablo Picasso', '1881', '1973', 'Spain', 'Modern', 'Cubism', 'A Spanish artist.'), 
('Juan Fernández', '1629', '1657', 'Spain', 'Baroque', 'Cubism', 'A Spanish artist.'), 
('Georges Braque', '1882', '1963', 'France', 'Fauvism', 'Cubism', 'A French artist.'), 
('Isidore Leroy', DEFAULT, DEFAULT, 'France', 'Fauvism', 'Cubism', 'A wallpaper manufacturer.'), 
('Louis Léopold Boilly', '1761', '1845', 'France', 'Realism', 'Baroque', 'A French painter and draftsman.'), 
('Niderviller', DEFAULT, DEFAULT, 'France', 'Trompe L\’oeil', 'Baroque', 'A French manufacturer of ceramics.'), 
('Vili', '1818', '1892', 'Kongo', 'Contemporary', 'Realism', 'Unknown'), 
('Simone Leigh', '1967', DEFAULT, 'United States', 'Contemporary', 'Contemporary', 'An American artist from Chicago.'), 
('David Drake', '1801', '1870', 'United States', 'Baroque', 'Baroque', 'An American potter.'), 
('Vincent van Gogh', '1853', '1890', 'Netherlands', 'Post-Impressionism', 'Post-Impressionism', 'A Dutch post-impressionist artist.'), 
('Giovanni Paolo Panini', '1691', '1765', 'Italy', 'Baroque', 'Baroque', 'An Italian painter and architect.'), 
('Lucas van Gassel', '1490', '1568', 'Netherlands', 'Baroque', 'Baroque', 'A Dutch painter.'), 
('Victor Janssens', '1701', '1769', 'Belgium', 'Baroque', 'Baroque', 'Unknown'),  
('Arthur Maees', '1628', '1697', 'Belgium', 'Baroque', 'Baroque', 'A Belgian sculptor.'), 
('Timothy Matthews', '1850', '1915', 'Britain', 'Baroque', 'Baroque', 'A British sculptor.'), 
('Guillaume Coustou', '1677', '1746', 'France', 'Baroque', 'Baroque', 'A French Sculptor.'), 
('Michelangelo', '1475', '1564', 'Italy', 'Renaissance', 'Renaissance', 'Italian sculptor and painter.'), 
('Leonardo da Vinci', '1452', '1519', 'Italy', 'Renaissance', 'Renaissance', 'An Italian polymath.'), 
('Jakob Blanck', '1640', '1713', 'France', 'Baroque', 'Baroque', 'A French goldsmith.'), 
('Eugène Delacroix', '1798', '1863', 'France', 'Romanticism', 'Baroque', 'A French artist.');

CREATE TABLE EXHIBITION
	(Exhibit_name		VARCHAR(80)				not null,
    Start_date			DATE					not null,
    End_date			DATE					not null,
    CONSTRAINT EXHPK PRIMARY KEY (Exhibit_name));

INSERT INTO EXHIBITION(Exhibit_name, Start_date, End_date)
VALUES
('The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08'), 
('Cubism and the Trompe l\’Oeil Tradition', '2022-10-20', '2023-01-22'), 
('Hear Me Now: The Black Potters of Old Edgefield, South Carolina', '2022-11-09', '2023-02-05'), 
('Van Gogh\'s Cypresses', '2023-05-22', '2023-08-27'), 
('The Rediscovery of The Baroque Period', '2022-08-01', '2022-11-01'), 
('Masterpieces of the Louvre', '2023-02-27', '2023-05-23');

CREATE TABLE ART_OBJECT
	(Id_no				VARCHAR(7)				not null,
    Title				VARCHAR(60)				default 'Unknown',
    Year_made			INTEGER, -- some values stored here are outside of domain for YEAR data type
    Origin				VARCHAR(20),
    Style				VARCHAR(20),
    Epoch				VARCHAR(20),
    Art_Desc			VARCHAR(60),
	Exhibit_name		VARCHAR(80)				default null,
	Artist_name			VARCHAR(40)				default null,
    CONSTRAINT OBJPK PRIMARY KEY (Id_no),
	CONSTRAINT OBJFK1 FOREIGN KEY (Exhibit_name) REFERENCES EXHIBITION(Exhibit_name)
		ON DELETE SET NULL			ON UPDATE CASCADE,
	CONSTRAINT OBJFK2 FOREIGN KEY (Artist_name) REFERENCES ARTIST(Artist_name)
		ON DELETE SET NULL			ON UPDATE CASCADE
    );
    
INSERT INTO ART_OBJECT (Id_no, Title, Year_made, Origin, Style, Epoch, Art_Desc, Exhibit_name, Artist_name)
VALUES
('AO_0001', 'Cup with cover', '1590', 'British, London', 'Renaissance', 'Renaissance', 'Crafted out of mother-of-pearl and exotic shells.','The Tudors: Art and Majesty in Renaissance England','R W'),
('AO_0002', 'Two-handled bowl', '1585', 'Chinese', 'Renaissance', 'Renaissance', 'A blue-and-white bowl made of Chinese porcelain.','The Tudors: Art and Majesty in Renaissance England', DEFAULT),
('AO_0003', 'Henry Frederick With Sir John Harington', '1603', 'British', 'Realism', 'Renaissance', 'Depicts a royal hunt with young Prince Henry.','The Tudors: Art and Majesty in Renaissance England','Robert Peake the Elder'),
('AO_0004', 'Portrait of a Man in Royal Livery', '1532', 'German', 'Realism', 'Renaissance', 'A man wearing royal livery.','The Tudors: Art and Majesty in Renaissance England','Hans Holbein the Younger'),
('AO_0005', 'Portrait Bust of John Fisher, Bishop of Rochester', '1515', 'Italian', 'Realism', 'Renaissance', 'Bust of John Fisher, Bishop of Rochester.','The Tudors: Art and Majesty in Renaissance England','Pietro Torrigiano'),
('AO_0006', 'Sprite', '1432', 'Italian', 'Early Renaissance', 'Renaissance', 'A sculpture made for a fountain.','The Tudors: Art and Majesty in Renaissance England','Donatello'),
('AO_0007', 'Virgin and Child', '1475', 'Italian', 'Romantic', 'Renaissance', 'A statue made in the style similar to Andrea\’s uncle.','The Tudors: Art and Majesty in Renaissance England','Andrea della Robbia'),
('AO_0008', 'Triton', '1594', 'Italian', 'Neoclassicism', 'Renaissance', 'A statue of a sea deity.','The Tudors: Art and Majesty in Renaissance England','Giambologna'),
('AO_0009', 'The Absinthe Glass', '1914', 'Spanish', 'Modern', 'Cubism', 'Life-sized rendering of a glass of alcohol.','Cubism and the Trompe l\’Oeil Tradition','Pablo Picasso'),
('AO_0010', 'Glass and Die', '1914', 'Spanish', 'Modern', 'Cubism', 'A deliberately rough-hewn composition.','Cubism and the Trompe l\’Oeil Tradition','Pablo Picasso'),
('AO_0011','Still Life with Four Bunches of Grapes','1636', 'Spanish', 'Baroque', 'Cubism', 'A bunch of grapes hanging in a dark chamber','Cubism and the Trompe l\’Oeil Tradition','Juan Fernández'),
('AO_0012', 'Still Life with Violin', '1912', 'French', 'Fauvism', 'Cubism', 'Strips of imitation wood-grain wallpaper on a drawing.','Cubism and the Trompe l\’Oeil Tradition','Georges Braque'), 
('AO_0013', 'Wallpaper: pattern 14020 F', '1902', 'French', 'Fauvism', 'Cubism', 'A blue and yellow flower-patterned wallpaper.','Cubism and the Trompe l\’Oeil Tradition','Isidore Leroy'),
('AO_0014', 'The Scallop Shell: Notre Avenir est dans l\'Air', '1912', 'Spanish', 'Modern', 'Cubism', 'Picasso\’s response to French Futurists.','Cubism and the Trompe l\’Oeil Tradition','Pablo Picasso'),
('AO_0015', 'Trompe l\’Oeil', '1804', 'French', 'Realism','Baroque', 'A piece with visual deceptions that \'fool the eye\'.','Cubism and the Trompe l\’Oeil Tradition','Louis Léopold Boilly'),
('AO_0016', 'Still Life', '1914', 'Spanish', 'Modern', 'Cubism', 'Includes playful allusions to trompe l’oeil painters.','Cubism and the Trompe l\’Oeil Tradition','Pablo Picasso'),
('AO_0017', 'Dessert plate', '1774', 'French', 'Trompe L\’oeil', 'Baroque', 'A print attached to a wood plate.','Cubism and the Trompe l\’Oeil Tradition','Niderviller'),
('AO_0018', 'Power figure', '1850', 'Kongo', 'Contemporary', 'Realism', 'A roughened iron statue.','Hear Me Now: The Black Potters of Old Edgefield, South Carolina','Vili'),
('AO_0019', '108 (Face Jug Series)', '2019', 'American', 'Contemporary', 'Contemporary', 'A porcelain jug of a face.','Hear Me Now: The Black Potters of Old Edgefield, South Carolina','Simone Leigh'),
('AO_0020', 'Storage jar', '1834', 'American', 'Baroque', 'Baroque', 'A simple, green stoneware pot.','Hear Me Now: The Black Potters of Old Edgefield, South Carolina','David Drake'),
('AO_0021', 'Garden at Arles', '1888', 'Dutch', 'Post-Impressionism', 'Post-Impressionism', 'A colourful painting of a flower garden.','Van Gogh\'s Cypresses','Vincent van Gogh'),
('AO_0022', 'Orchard Bordered by Cypresses', '1888', 'Dutch', 'Post-Impressionism', 'Post-Impressionism', 'A painting of a cloudy day in an orchard.','Van Gogh\'s Cypresses','Vincent van Gogh'),
('AO_0023', 'Vue du Forum à Rome', '1740', 'Italian', 'Baroque', 'Baroque', 'Artwork recovered after World War II.','The Rediscovery of The Baroque Period','Giovanni Paolo Panini'),
('AO_0024', 'Vue d\'une ville fortifiée avec un port', '1520', 'Dutch', 'Baroque', 'Baroque', 'Artwork recovered after World War II.','The Rediscovery of The Baroque Period','Lucas van Gassel'),
('AO_0025', 'Zéphyr porte les sœurs de Psyché au palais de l\'Amour', '1725', 'Belgian', 'Baroque', 'Baroque', 'A tapestry depicting Psyche and her three attendants.','The Rediscovery of The Baroque Period','Victor Janssens'),
('AO_0026', 'Vitrail : trois panneaux', '1730', 'French', 'Baroque', 'Baroque', 'Black and white stained glass.','The Rediscovery of The Baroque Period', DEFAULT),
('AO_0027', 'Statuette : la Vierge à l\'Enfant', '1671', 'Belgian', 'Baroque', 'Baroque', 'Artwork recovered after World War II.','The Rediscovery of The Baroque Period','Arthur Maees'),
('AO_0028', 'Pied de meuble d\'un groupe de trois', '1893', 'British', 'Baroque', 'Baroque', 'Artwork recovered after World War II.','The Rediscovery of The Baroque Period','Timothy Matthews'),
('AO_0029', 'Cheval retenu par un palefrenier', '1745', 'French', 'Baroque', 'Baroque', 'A horse and a man.','Masterpieces of the Louvre','Guillaume Coustou'),
('AO_0030', 'Esclave rebelle', '1515', 'Italian', 'Renaissance', 'Renaissance', 'A statue of a rebel slave.','Masterpieces of the Louvre','Michelangelo'),
('AO_0031', 'Mona Lisa', '1503', 'Italian', 'Renaissance', 'Renaissance', 'A portrait painting.','Masterpieces of the Louvre','Leonardo da Vinci'),
('AO_0032', 'Coffre des pierreries de Louis XIV', '1677', 'French', 'Baroque', 'Baroque', 'A gold chest of jewels.','Masterpieces of the Louvre','Jakob Blanck'),
('AO_0033', 'Liberty Leading the People', '1830', 'French', 'Romanticism', 'Baroque', 'A painting commemorating the French Revolution of 1830.','Masterpieces of the Louvre','Eugène Delacroix'),
('AO_0034', 'The Monzon Lion', '1100', 'Spanish', 'Ancient', 'Ancient', 'A sculpture of a lion.','Masterpieces of the Louvre', DEFAULT);

CREATE TABLE PAINTING
	(Id_no				VARCHAR(7)				not null,
    Paint_type			VARCHAR(15),
    Drawn_on			VARCHAR(15),
    CONSTRAINT PAIPK PRIMARY KEY (Id_no),
    CONSTRAINT PAIFK1 FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
		ON DELETE CASCADE			ON UPDATE CASCADE);

INSERT INTO PAINTING (Id_no, Paint_type, Drawn_on)
VALUES
('AO_0003', 'Oil', 'Canvas'), 
('AO_0004', 'Oil and gold', 'Parchment'), 
('AO_0011', 'Oil', 'Canvas'), 
('AO_0014', 'Oil and enamel', 'Canvas'), 
('AO_0021', 'Oil', 'Canvas'), 
('AO_0022', 'Oil', 'Canvas'), 
('AO_0023', 'Oil', 'Canvas'), 
('AO_0024', 'Oil', 'Wood'), 
('AO_0031', 'Oil', 'Wood'), 
('AO_0033', 'Oil', 'Canvas');

CREATE TABLE SCULPTURE_OR_STATUE
	(Id_no				VARCHAR(7)				not null,
    Material			VARCHAR(50),
    Height				DECIMAL(10, 2),
    Weight				DECIMAL(10, 2),
    CONSTRAINT STAPK PRIMARY KEY (Id_no),
    CONSTRAINT SCUFK1 FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
		ON DELETE CASCADE			ON UPDATE CASCADE);

INSERT INTO SCULPTURE_OR_STATUE (Id_no, Material, Height, Weight)
VALUES
('AO_0005', 'Polychrome terracotta', '61.6', '28.1'), 
('AO_0006', 'High-copper alloy, fire-gilt, brown natural patina', '61.6', '13.6'), 
('AO_0009', 'Painted bronze and perforated tin absinthe spoon', '22.5', '3.6'), 
('AO_0010', 'Painted wood', '23.5', '2.4'), 
('AO_0016', 'Painted wood and fabric upholstery fringe', '25.4', '3.0'), 
('AO_0027', 'Bronze', '16.2', '6.9'), 
('AO_0029', 'Carrara Marble', '340.0', '542.6'),
('AO_0007','Marble','94.9','32.8'),
('AO_0008','Limestone','91.4','24.4'),
('AO_0015','Bronze','74.3','23.7'),
('AO_0018','Wood and Iron and Fibre','103.5','18.1'),
('AO_0028','Hardstone','25.7','11.4'),
('AO_0030','Marble','215.0','194.5'),
('AO_0034','Metal','54.5','10.83');

CREATE TABLE OTHER
	(Id_no				VARCHAR(7)				not null,
    Art_type			VARCHAR(15)				not null,
    CONSTRAINT OTHPK PRIMARY KEY (Id_no),
    CONSTRAINT OTHFK1 FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
		ON DELETE CASCADE			ON UPDATE CASCADE);

INSERT INTO OTHER (Id_no, Art_type)
VALUES
('AO_0001','Metalwork'),
('AO_0002','Metalwork'),
('AO_0012','Collage'),
('AO_0013','Wallpaper'),
('AO_0017','Ceramics'),
('AO_0019','Ceramics'),
('AO_0020','Stoneware'),
('AO_0025','Tapestry'),
('AO_0026','Stained glass'),
('AO_0032','Gold chest');

CREATE TABLE COLLECTION
	(Coll_name			VARCHAR(30)				not null,
    Coll_type			VARCHAR(15)				not null,
    Phone				VARCHAR(15)				not null,
    Contact_person		VARCHAR(20),
    Epoch				VARCHAR(20),
    Coll_desc			VARCHAR(100),
    CONSTRAINT COLPK PRIMARY KEY (Coll_name));

INSERT INTO COLLECTION (Coll_name, Coll_type, Phone, Contact_person, Epoch, Coll_desc)
VALUES
('National Museums Recovery','Museum','33-010-111-1111','Leslie Davis','Multiple','Art pieces from the Baroque period.'),
('Masterpieces of the Louvre','Museum','33-010-111-1111','Leslie Davis','Multiple','Essential artworks to the Louvre.');

CREATE TABLE PERMANENT_COLLECTION
	(Id_no				VARCHAR(7)				not null,
    Date_acquired		DATE					not null,
    Pcoll_status		VARCHAR(10)				not null,
    Cost				DECIMAL(10, 2),
    CONSTRAINT PERPK PRIMARY KEY (Id_no),
    CONSTRAINT PERFK1 FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
		ON DELETE CASCADE			ON UPDATE CASCADE);

INSERT INTO PERMANENT_COLLECTION (Id_no, Date_acquired, Pcoll_status, Cost)
VALUES
('AO_0001','1977-09-29','On loan','116085.89'),
('AO_0002','1914-02-17','On display','140293.52'),
('AO_0003','1952-10-07','Stored','223122.34'),
('AO_0004','2022-10-10','On display','213432.32'),
('AO_0005','2022-10-10','On display','163043.33'),
('AO_0006','2008-10-24','On display','180025.67'),
('AO_0007','1957-01-30','Stored','153438.66'),
('AO_0008','1913-08-12','On loan','120387.56'),
('AO_0009','1997-08-26','On loan','245346.55'),
('AO_0010','2022-10-17','Stored','214395.89'),
('AO_0011','2022-10-17','On display','192347.58'),
('AO_0012','2022-10-17','On display','130029.71'),
('AO_0013','2021-06-12','On display','100348.54'),
('AO_0014','1980-09-16','On loan','230455.65'),
('AO_0015','2022-10-17','On loan','244396.45'),
('AO_0016','2022-10-17','On display','136454.46'),
('AO_0017','2022-10-17','On display','80564.58'),
('AO_0018','2011-07-20','On loan','60453.70'),
('AO_0019','2020-04-11','On display','50342.88'),
('AO_0020','2002-03-15','On display','61430.39'),
('AO_0021','2023-05-22','On display','730324.34'),
('AO_0022','2023-05-22','On display','757933.86');

CREATE TABLE BORROWED
	(Id_no				VARCHAR(7)				not null,
	Coll_name			VARCHAR(30)				not null,
    Date_borrowed		DATE					not null,
    Date_returned		DATE,
    CONSTRAINT PAIPKId PRIMARY KEY (Id_no),
    CONSTRAINT BORFK1 FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
		ON DELETE CASCADE			ON UPDATE CASCADE,
    CONSTRAINT BORFK2 FOREIGN KEY (Coll_name) REFERENCES COLLECTION(Coll_name)
		ON DELETE CASCADE			ON UPDATE CASCADE);
    
INSERT INTO BORROWED (Id_no, Coll_name, Date_borrowed, Date_returned)
VALUES
('AO_0023','National Museums Recovery','2023-06-10','2023-10-05'),
('AO_0024','National Museums Recovery','2023-06-10','2023-10-05'),
('AO_0025','National Museums Recovery','2023-06-10','2023-10-05'),
('AO_0026','National Museums Recovery','2023-06-10','2023-10-05'),
('AO_0027','National Museums Recovery','2023-06-10','2023-10-05'),
('AO_0028','National Museums Recovery','2023-06-10','2023-10-05'),
('AO_0029','Masterpieces of the Louvre','2023-02-20','2023-05-30'),
('AO_0030','Masterpieces of the Louvre','2023-02-20','2023-05-30'),
('AO_0031','Masterpieces of the Louvre','2023-02-20','2023-05-30'),
('AO_0032','Masterpieces of the Louvre','2023-02-20','2023-05-30'),
('AO_0033','Masterpieces of the Louvre','2023-02-20','2023-05-30'),
('AO_0034','Masterpieces of the Louvre','2023-02-20','2023-05-30');

-- custom triggers, also in query file for ease of reading

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
