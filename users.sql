//for creating the table Users:


create table Users(userid varchar(45),username char(45),password varchar(45));
 ALTER table Users add PRIMARY KEY(userid);
                                               

                                                                         
//for creating a stored procedure:
                                                                         
                                                                         
 DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `User`(
    IN p_name VARCHAR(20),
    IN p_username VARCHAR(20),
    IN p_password VARCHAR(20)
)
BEGIN
    if ( select exists (select 1 from Users where username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into Users
        (
            username,
            userid,
            password
        )
        values
        (
            p_name,
            p_username,
            p_password
        );
     
    END IF;
END$$
DELIMITER ;                                                                      
                                                                         
                                                                         
                                                                         
                                                                         
                                                                        
