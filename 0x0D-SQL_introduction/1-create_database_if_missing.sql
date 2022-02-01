--Creates the database hbtn_0c_0
--If it already exists,it doesn't fail
IF (EXISTS)
BEGIN
	print 'Database already exists'
END;
ELSE
BEGIN
	CREATE DATABASE hbtn_0c_0;
END;
