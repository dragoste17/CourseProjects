<?php
$servername = "localhost";
$username = "root";
$password = "";

// Create connection
$conn = new mysqli($servername, $username, $password);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

// Create database
$sql = "CREATE DATABASE cspprojectdatabase";
if ($conn->query($sql) === TRUE) {
    echo "Database created successfully";
} else {
    echo "Error creating database: " . $conn->error;
}
$servername = "localhost";
$username = "root";
$password = "";
$myDb='cspprojectdatabase';
// Create connection
$conn = new mysqli($servername, $username, $password,$myDb);


$sql = "CREATE TABLE user (
id VARCHAR(40) , 
leaves INT(3),
level INT(1) ,
name VARCHAR(40) NOT NULL,
password VARCHAR(40) NOT NULL ,
leaves2 INT(3) ,
leaves3 INT(3) ,
leaves4 INT(3)
)";

if ($conn->query($sql) === TRUE) {
    echo "Database created successfully";
} else {
    echo "Error creating database: " . $conn->error;
}

$sql = "CREATE TABLE dashboard (
applicant VARCHAR(40) NOT NULL,
content text,
date VARCHAR(11),
id VARCHAR(40) ,
subject VARCHAR(100) , 
LeavesNeeded INT(3) ,
TypeOfLeave VARCHAR(20)
 
)";

if ($conn->query($sql) === TRUE) {
    echo "Database created successfully";
} else {
    echo "Error creating database: " . $conn->error;
}

$sql = "INSERT INTO user (id,leaves,level,name,password, leaves2, leaves3, leaves4)
			VALUES ('id3@gmail.com','14','3','Head','abcd','4','7','10')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();

?>
