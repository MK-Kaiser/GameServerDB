-- This file displays some combined data through joins and begins setting up data manipulation callbacks that will be triggered from our webpage

-----------------------------------------------------
-- Joined table examples
-----------------------------------------------------

-- Select all users by full name, character names, character level, ordered by user name
SELECT CONCAT(GameUsers.firstName, ' ', GameUsers.lastName) as UserName, GameCharacters.charName as CharName, GameCharacters.level as CharLevel
FROM GameUsers
INNER JOIN GameCharacters ON GameUsers.userId = GameCharacters.userId
ORDER BY UserName ASC;

-- Select available recipes for each character based on their profession and character level
SELECT GameCharacters_Professions.charName as CharName, GameCharacters.level as CharLevel, GameProfessionsRecipes.recipeName as AvailableRecipes, GameProfessionsRecipes.levelRequirement as RecipeReqLevel
FROM GameProfessionsRecipes
LEFT JOIN GameProfessions ON GameProfessionsRecipes.professionId = GameProfessions.professionId
LEFT JOIN GameCharacters_Professions ON GameProfessions.professionId = GameCharacters_Professions.professionId
LEFT JOIN GameCharacters ON GameCharacters_Professions.charName = GameCharacters.charName
WHERE GameCharacters.level >= GameProfessionsRecipes.levelRequirement
ORDER BY GameCharacters.charName ASC;

-- Select each characters guilds by name
SELECT GameCharacters.charName, GameGuilds.guildName
FROM GameCharacters
LEFT JOIN GameCharacters_Guilds ON GameCharacters.charName = GameCharacters_Guilds.charName
LEFT JOIN GameGuilds ON GameCharacters_Guilds.guildId = GameGuilds.guildId;


-----------------------------------------------------
-- Web page UI manipulation callbacks
-----------------------------------------------------

-- GameUsers manipulation (Add, Edit, Delete). Only allowing editing password of existing user.
INSERT INTO GameUsers (firstName, lastName, userEmail, password) VALUES (:firstNameInput, :lastNameInput, :userEmailInput, :passwordInput);
UPDATE GameUsers SET password = :passwordUpdateInput;
DELETE FROM GameUsers WHERE userEmail = :userEmailDeleteInput;

-- GameCharacters manipulation (Add, Edit, Delete)
INSERT INTO GameCharacters (charName, userId) VALUES (:charNameInput, (SELECT userId FROM GameUsers WHERE userEmail = :userEmailInput));
UPDATE GameCharacters SET level = :levelUpdateInput, charName = :charNameUpdateInput;
DELETE FROM GameCharacters WHERE charName = :charNameDeleteInput;

-- GameProfessions manipulation (Add, Edit, Delete). Do we want to allow add by anyone for this project?
INSERT INTO GameProfessions (professionName) VALUES (:professionNameInput);
UPDATE GameProfessions SET professionName = :professionNameUpdateInput;
DELETE FROM GameProfessions WHERE professionName = :professionNameDeleteInput;

-- GameGuilds manipulation (Add, Edit, Delete)
INSERT INTO GameGuilds (guildName) VALUES (:guildNameInput);
UPDATE GameGuilds SET guildName = :guildNameUpdateInput;
DELETE FROM GameGuilds WHERE guildName = :guildNameDeleteInput;

-- Create a new profession recipe (should only work if profession has already been inserted in Profession table)
INSERT INTO GameProfessionsRecipes (recipeName, professionId, levelRequirement) VALUES (:recipeNameInput, (SELECT professionId FROM GameProfessions WHERE professionName = :professionNameInput), :levelRequirementInput);
UPDATE GameProfessionsRecipe SET recipeName = :recipeNameUpdateInput, professionId = :professionIdUpdateInput, levelRequirement = :levelRequirementUpdateInput;
DELETE FROM GameProfessionsRecipe WHERE recipeName = :recipeNameDeleteInput;

-- Add a profession to a character (profession must exist in profession table first)
INSERT INTO GameCharacters_Professions (charName, professionId) VALUES (:charNameInput, (SELECT professionId FROM GameProfessions WHERE professionName = :professionNameInput));
DELETE FROM GameCharacters_Professions WHERE charName = :charNameProfessionDeleteInput AND professionId = :professionIdDeleteInput;

-- Add a character to a guild (guild must exist in guild table first)
INSERT INTO GameCharacters_Guilds (charName, guildId) VALUES (:charNameInput, (SELECT guildId FROM GameGuilds WHERE guildName = :guildNameInput));
DELETE FROM GameCharacters_Guilds WHERE charName = :charNameGuildDeleteInput AND guildId = guildIdDeleteInput;
