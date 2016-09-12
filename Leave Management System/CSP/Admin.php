	<?php
	$servername = "localhost";
	$username = 'root';
	$password = '';
	$dbname = 'cspprojectdatabase';
	// Create connection
	$conn = mysqli_connect($servername, $username, $password, $dbname) or die("Failed to connect to MySQL: " . mysql_error());	
	// Check connection
	if (!$conn) {
	    die("Connection failed: " . mysqli_connect_error());
	}


	echo "<!DOCTYPE html>
	<html>
	<body>
		<h1>Admin Account</h1><br>
		";
		echo "<h2>Profile information</h2><hr><br>";
		echo "	
		<table style='width:100%'>
			<tr>";
				echo "
				<td>Name</td>
				<td>ID</td>		
				<td>Level</td>
				<td>Leaves type1</td>
				<td>Leaves type2</td>
				<td>Leaves type3</td>
				<td>Leaves type4 </td>
			</tr>";

	$sql = "SELECT * FROM user";
	$result = mysqli_query($conn, $sql);

	if (mysqli_num_rows($result) > 0) {
	    
	    while($row = mysqli_fetch_assoc($result)) {
	        echo '
	        <tr>
	        <td>'. $row["name"]. '</td>
	    	<td>'. $row["id"].' </td>
	    	<td>'. $row["level"].' </td>
	    	<td>'. $row["leaves"].' </td>
	    	<td>'. $row["leaves2"].' </td>
	    	<td>'. $row["leaves3"].' </td>
	    	<td>'. $row["leaves4"]. '</td>
	    	</tr>';
	    }
	} else {
	    echo "0 results";
	}
echo "</table>";
		echo "<br><br><br><h2>Application information</h2><hr><br>";
		echo '	
		<table style="width:100%">
			<tr>
				
				<td>From</td>
				<td>Date Applied at</td>		
				<td>Number of Leaves</td>
				<td>To</td>
				<td>Type of leave</td>
			</tr>';

	$sql = "SELECT * FROM dashboard where Subject='Applications'";
	$result = mysqli_query($conn, $sql);

	if (mysqli_num_rows($result) > 0) {
	    
	    while($row = mysqli_fetch_assoc($result)) {
	        echo '
	        <tr>
	        <td>'. $row["applicant"]. '</td>
	    	<td>'. $row["date"].' </td>
	    	<td>'. $row["LeavesNeeded"].' </td>
	    	<td>'. $row["id"].' </td>
	    	<td>'. $row["TypeOfLeave"].' </td>
	    	</tr>';
	    }
	} else {
	    echo "0 results";
	}


	echo "</table>";
echo "<br><br><br><h2>Responses information</h2><hr><br>";
		echo '	
		<table style="width:100%">
			<tr>
				
				<td>From</td>
				<td>Date Applied at</td>		
				<td>Number of Leaves</td>
				<td>Approved By</td>
				<td>Leaves type of leave</td>
			</tr>';

	$sql = "SELECT * FROM dashboard where Subject='Responses'";
	$result = mysqli_query($conn, $sql);

	if (mysqli_num_rows($result) > 0) {
	    
	    while($row = mysqli_fetch_assoc($result)) {
	        echo '
	        <tr>
	        <td>'. $row["id"]. '</td>
	    	<td>'. $row["date"].' </td>
	    	<td>'. $row["LeavesNeeded"].' </td>
	    	<td>'. $row["applicant"].' </td>
	    	<td>'. $row["TypeOfLeave"].' </td>
	    	</tr>';
	    }
	} else {
	    echo "0 results";
	}


	mysqli_close($conn);
	echo "</table><br><br><br><br><br><br>";
		?>
