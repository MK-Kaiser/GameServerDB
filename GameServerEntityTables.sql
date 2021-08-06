DROP TABLE IF EXISTS GameCharacters_Professions;
DROP TABLE IF EXISTS GameCharacters_Guilds;
DROP TABLE IF EXISTS GameProfessionsRecipes;
DROP TABLE IF EXISTS GameProfessions;
DROP TABLE IF EXISTS GameGuilds;
DROP TABLE IF EXISTS GameCharacters;
DROP TABLE IF EXISTS GameUsers;

CREATE TABLE GameUsers(
    userId int(11) NOT NULL AUTO_INCREMENT,
    userEmail varchar(255) NOT NULL UNIQUE,
    firstName varchar(255) NOT NULL,
    lastName varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    PRIMARY KEY(userId)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE GameCharacters(
    charName varchar(255) NOT NULL UNIQUE,
    userId int(11) NOT NULL,
    level int(11) DEFAULT 1,
    FOREIGN KEY (userId) REFERENCES GameUsers(userId) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY(charName)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE GameGuilds(
    guildId int(11) NOT NULL AUTO_INCREMENT,
    guildName varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY(guildId)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE GameProfessions(
    professionId int(11) NOT NULL AUTO_INCREMENT,
    professionName varchar(255) NOT NULL UNIQUE,
    PRIMARY KEY(professionId)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE GameProfessionsRecipes(
    recipeId int(11) NOT NULL AUTO_INCREMENT,
    recipeName varchar(255) NOT NULL UNIQUE,
    professionId int(11) DEFAULT NULL,
    levelRequirement int(11) DEFAULT 1,
    FOREIGN KEY (professionId) REFERENCES GameProfessions(professionId) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY(recipeId)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE GameCharacters_Professions(
    charName varchar(255) NOT NULL,
    professionId int(11) NOT NULL,
    FOREIGN KEY (charName) REFERENCES GameCharacters(charName) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (professionId) REFERENCES GameProfessions(professionId) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (charName, professionId)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE GameCharacters_Guilds(
    charName varchar(255) NOT NULL,
    guildId int(11) NOT NULL,
    FOREIGN KEY (charName) REFERENCES GameCharacters(charName) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (guildId) REFERENCES GameGuilds(guildId) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (charName, guildId)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


LOCK TABLES GameUsers WRITE;
INSERT INTO GameUsers (firstName, lastName, userEmail, password) VALUES ("Jo", "Smith", "johnsmith@aol.com", "password1!");
INSERT INTO GameUsers (firstName, lastName, userEmail, password) VALUES ("samantha", "jones", "sjones@yahoo.com", "otherPassword32");
INSERT INTO GameUsers (firstName, lastName, userEmail, password) VALUES ("Bradley", "Boseman", "bbose@gmail.com", "bbosem");
INSERT INTO GameUsers (firstName, lastName, userEmail, password) VALUES ("henry", "hoover", "hehoo@hotmail.com", "theyllneverguessit");
INSERT INTO GameUsers (firstName, lastName, userEmail, password) VALUES ("Bob", "bobert", "bobob@specialdomain.com", "complexpassword");
UNLOCK TABLES;

LOCK TABLES GameCharacters WRITE;
LOCK TABLES GameUsers WRITE;
INSERT INTO GameCharacters (charName, userId) VALUES ("Zezoo", (SELECT userId FROM GameUsers WHERE userEmail = "johnsmith@aol.com")); -- use default level value, 1
INSERT INTO GameCharacters (charName, userId, level) VALUES ("Ryu", (SELECT userId FROM GameUsers WHERE userEmail = "sjones@yahoo.com"), 1);
INSERT INTO GameCharacters (charName, userId, level) VALUES ("Ken", (SELECT userId FROM GameUsers WHERE userEmail = "sjones@yahoo.com"), 3);
INSERT INTO GameCharacters (charName, userId, level) VALUES ("Goliath", (SELECT userId FROM GameUsers WHERE userEmail = "hehoo@hotmail.com"), 1);
INSERT INTO GameCharacters (charName, userId, level) VALUES ("Batman", (SELECT userId FROM GameUsers WHERE userEmail = "bobob@specialdomain.com"), 1);
UNLOCK TABLES;


LOCK TABLES GameProfessions WRITE;
INSERT INTO GameProfessions (professionName) VALUES ("Alchemy");
INSERT INTO GameProfessions (professionName) VALUES ("Blacksmithing");
INSERT INTO GameProfessions (professionName) VALUES ("Enchanting");
INSERT INTO GameProfessions (professionName) VALUES ("Engineering");
INSERT INTO GameProfessions (professionName) VALUES ("Herbalism");
INSERT INTO GameProfessions (professionName) VALUES ("Mining");
UNLOCK TABLES;

LOCK TABLES GameGuilds WRITE;
INSERT INTO GameGuilds (guildName) VALUES ("The Green Hornets");
INSERT INTO GameGuilds (guildName) VALUES ("The Best Guild");
INSERT INTO GameGuilds (guildName) VALUES ("Trolls R Us");
INSERT INTO GameGuilds (guildName) VALUES ("Knights of Azmodan");
INSERT INTO GameGuilds (guildName) VALUES ("Manchester United");
UNLOCK TABLES;

LOCK TABLES GameProfessionsRecipes WRITE;
LOCK TABLES GameProfessions WRITE;
INSERT INTO GameProfessionsRecipes (recipeName, professionId) VALUES ("Small Health Potion", (SELECT professionId FROM GameProfessions WHERE professionName = "Alchemy")); -- first recipe, use default value
INSERT INTO GameProfessionsRecipes (recipeName, professionId, levelRequirement) VALUES ("Medium Health Potion", (SELECT professionId FROM GameProfessions WHERE professionName = "Alchemy"), 35);
INSERT INTO GameProfessionsRecipes (recipeName, professionId, levelRequirement) VALUES ("Large Health Potion", (SELECT professionId FROM GameProfessions WHERE professionName = "Alchemy"), 55);

INSERT INTO GameProfessionsRecipes (recipeName, professionId) VALUES ("Leather Cuirass", (SELECT professionId FROM GameProfessions WHERE professionName = "Blacksmithing"));
INSERT INTO GameProfessionsRecipes (recipeName, professionId, levelRequirement) VALUES ("Steel Cuirass", (SELECT professionId FROM GameProfessions WHERE professionName = "Blacksmithing"), 45);
INSERT INTO GameProfessionsRecipes (recipeName, professionId, levelRequirement) VALUES ("Diamond Cuirass", (SELECT professionId FROM GameProfessions WHERE professionName = "Blacksmithing"), 75);

INSERT INTO GameProfessionsRecipes (recipeName, professionId) VALUES ("Enchantment of Minor Strength", (SELECT professionId FROM GameProfessions WHERE professionName = "Enchanting"));
INSERT INTO GameProfessionsRecipes (recipeName, professionId, levelRequirement) VALUES ("Enchantment of Moderate Strength", (SELECT professionId FROM GameProfessions WHERE professionName = "Enchanting"), 15);
INSERT INTO GameProfessionsRecipes (recipeName, professionId, levelRequirement) VALUES ("Enchantment of Major Strength", (SELECT professionId FROM GameProfessions WHERE professionName = "Enchanting"), 40);

INSERT INTO GameProfessionsRecipes (recipeName, professionId) VALUES ("Telescope", (SELECT professionId FROM GameProfessions WHERE professionName = "Engineering"));
INSERT INTO GameProfessionsRecipes (recipeName, professionId, levelRequirement) VALUES ("Zipline", (SELECT professionId FROM GameProfessions WHERE professionName = "Engineering"), 5);
INSERT INTO GameProfessionsRecipes (recipeName, professionId, levelRequirement) VALUES ("Wormhole Generator", (SELECT professionId FROM GameProfessions WHERE professionName = "Engineering"), 15);

INSERT INTO GameProfessionsRecipes (recipeName, professionId) VALUES ("Minor Rejuvenating Salve", (SELECT professionId FROM GameProfessions WHERE professionName = "Herbalism"));
INSERT INTO GameProfessionsRecipes (recipeName, professionId, levelRequirement) VALUES ("Moderate Rejuvenating Salve", (SELECT professionId FROM GameProfessions WHERE professionName = "Herbalism"), 15);
INSERT INTO GameProfessionsRecipes (recipeName, professionId, levelRequirement) VALUES ("Major Rejuvenating Salve", (SELECT professionId FROM GameProfessions WHERE professionName = "Herbalism"), 35);

INSERT INTO GameProfessionsRecipes (recipeName, professionId) VALUES ("Wooden Pick", (SELECT professionId FROM GameProfessions WHERE professionName = "Mining"));
INSERT INTO GameProfessionsRecipes (recipeName, professionId, levelRequirement) VALUES ("Steel Pick", (SELECT professionId FROM GameProfessions WHERE professionName = "Mining"), 15);
INSERT INTO GameProfessionsRecipes (recipeName, professionId, levelRequirement) VALUES ("Diamond Pick", (SELECT professionId FROM GameProfessions WHERE professionName = "Mining"), 60);
UNLOCK TABLES;

LOCK TABLES GameCharacters_Professions WRITE;
LOCK TABLES GameCharacters WRITE;
LOCK TABLES GameProfessions WRITE;
INSERT INTO GameCharacters_Professions (charName, professionId) VALUES ("Zezoo", (SELECT professionId FROM GameProfessions WHERE professionName = "Alchemy"));
INSERT INTO GameCharacters_Professions (charName, professionId) VALUES ("Zezoo", (SELECT professionId FROM GameProfessions WHERE professionName = "Engineering"));
INSERT INTO GameCharacters_Professions (charName, professionId) VALUES ("Ryu", (SELECT professionId FROM GameProfessions WHERE professionName = "Blacksmithing"));
INSERT INTO GameCharacters_Professions (charName, professionId) VALUES ("Goliath", (SELECT professionId FROM GameProfessions WHERE professionName = "Enchanting"));
INSERT INTO GameCharacters_Professions (charName, professionId) VALUES ("Ken", (SELECT professionId FROM GameProfessions WHERE professionName = "Engineering"));
INSERT INTO GameCharacters_Professions (charName, professionId) VALUES ("Ken", (SELECT professionId FROM GameProfessions WHERE professionName = "Herbalism"));
INSERT INTO GameCharacters_Professions (charName, professionId) VALUES ("Ken", (SELECT professionId FROM GameProfessions WHERE professionName = "Mining"));
UNLOCK TABLES;

LOCK TABLES GameCharacters_Guilds WRITE;
LOCK TABLES GameCharacters WRITE;
LOCK TABLES GameGuilds WRITE;
INSERT INTO GameCharacters_Guilds (charName, guildId) VALUES ("Zezoo", (SELECT guildId FROM GameGuilds WHERE guildName = "The Green Hornets"));
INSERT INTO GameCharacters_Guilds (charName, guildId) VALUES ("Ryu", (SELECT guildId FROM GameGuilds WHERE guildName = "The Green Hornets"));
INSERT INTO GameCharacters_Guilds (charName, guildId) VALUES ("Goliath", (SELECT guildId FROM GameGuilds WHERE guildName = "The Best Guild"));
INSERT INTO GameCharacters_Guilds (charName, guildId) VALUES ("Ken", (SELECT guildId FROM GameGuilds WHERE guildName = "Knights of Azmodan"));
INSERT INTO GameCharacters_Guilds (charName, guildId) VALUES ("Ken", (SELECT guildId FROM GameGuilds WHERE guildName = "Manchester United"));
INSERT INTO GameCharacters_Guilds (charName, guildId) VALUES ("Ken", (SELECT guildId FROM GameGuilds WHERE guildName = "The Best Guild"));
UNLOCK TABLES;
