<?php
$servername = "localhost";
$username = 'root';
$password = '';
$dbname = 'cspprojectdatabase';
$conn = mysqli_connect($servername, $username, $password, $dbname) or die("Failed to connect to MySQL: " . mysql_error());	

$from='from';	
$to='emailaddress';
$content='description';
$sub='subject';
$startLeave=3;
$endLeave=6;
$LeavesNeeded=-1;
$MyDate='12-12-2015';
function PostTODashboard()
{
	global $conn;	
	global $to,$from,$content,$sub,$MyDate,$LeavesNeeded,$TypeOfLeave;
	if ($LeavesNeeded<0){
		$sql = "INSERT INTO dashboard ".
		"(id,content,date,applicant,subject,TypeOfLeave) ".
		"VALUES('$to','$content','$MyDate','$from','$sub','$TypeOfLeave')";
		if (mysqli_query($conn, $sql)) {
			echo "Application has been posted successfully";
			$sql="SELECT password FROM user where id='$from'";
			$result=mysqli_query($conn,$sql);
			$row=mysqli_fetch_assoc($result);
			echo '<form action="connectivity.php" method="POST">
			<input name="user" value='.$from.' style="visibility:hidden;">
			<input name="pass" value='.$row["password"].' style="visibility:hidden;">	
			<br>
			<input id="button" type="submit" name="sign_in" value="Click here to go back.">
			
			</form>';
		} else {
			echo "Error: " . $sql . "<br>" . mysqli_error($conn);
		}
	}
	else{
$sql = "INSERT INTO dashboard ".
		"(id,content,date,applicant,subject,LeavesNeeded,TypeOfLeave) ".
		"VALUES('$to','$content','$MyDate','$from','$sub','$LeavesNeeded','$TypeOfLeave')";
		if (mysqli_query($conn, $sql)) {
		$sql="SELECT password FROM user where id='$from'";
			$result=mysqli_query($conn,$sql);
			$row=mysqli_fetch_assoc($result);
		
			echo "Application has been posted successfully";
		echo '<form action="connectivity.php" method="POST">
			<input name="user" value='.$from.' style="visibility:hidden;">
			<input name="pass" value='.$row["password"].' style="visibility:hidden;" >	
			<br>
			<input id="button" type="submit" name="sign_in" value="Click here to go back.">
			
			</form>';
				
			
			
		} else {
			echo "Error: " . $sql . "<br>" . mysqli_error($conn);
		}


}
	
}


function DecrementLeaves()
{
	global $to,$from,$content,$sub,$MyDate,$LeavesNeeded,$TypeOfLeave;
	global $conn;
	$sql="SELECT '$TypeOfLeave' FROM user WHERE id='$to'";
	$result=mysqli_query($conn,$sql);
	$row = mysqli_fetch_row($result) or die(mysql_error());
	$LeavesLeft=((int)$row[0]) - $LeavesNeeded;
	$sql="UPDATE user SET $TypeOfLeave='$LeavesLeft' WHERE id='$to'";
	mysqli_query($conn,$sql);
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') { 
	global $to,$from,$content,$sub,$MyDate,$leaves;
	global $conn;
	if (isset($_POST['SubmitApplication'])) {
		global $conn;
		$fro123=$_POST['from'];
		$from = mysqli_real_escape_string($conn,$fro123);
		$t123=$_POST['emailaddress'];
		$to = mysqli_real_escape_string($conn,$t123);
		$conten123=$_POST['description'];
		$content = mysqli_real_escape_string($conn,$conten123);
		$sub123=$_POST['subject'];
		$sub = mysqli_real_escape_string($conn,$sub123);
		$TypeOfLeave=$_POST['TypeOfLeave'];
		$startLeave=date_create($_POST['start']);
		$endLeave=date_create($_POST['end']);
		$diff= date_diff($startLeave, $endLeave);
		$LeavesNeeded= $diff->format("%a");
		$LeavesNeeded+=1;
		$MyDate=date_format($startLeave,"d-m-Y");
		PostToDashBoard();
	} 
	else if (isset($_POST['level3_approve'])) {
		global $to,$from,$content,$sub,$MyDate;
		global $conn;
		$to123=$_POST['to'];
		$to = mysqli_real_escape_string($conn,$to123);
		$TypeOfLeave=$_POST['TypeOfLeave'];
		$from123=$_POST['from'];
		$from = mysqli_real_escape_string($conn,$from123);
		$MyDate123=$_POST['date'];
		$MyDate = mysqli_real_escape_string($conn,$MyDate123);
		$content="your application for leave posted on ".$MyDate." has been sanctioned by ".$from;
		$sub='Responses';
		$LeavesNeeded123=(int)$_POST['LeavesNeeded'];
		$LeavesNeeded = mysqli_real_escape_string($conn,$LeavesNeeded123);
		PostToDashBoard();
		DecrementLeaves();
	}	
	else if (isset($_POST['level2_approve'])) {
		global $to,$from,$content,$sub,$MyDate,$TypeOfLeave;
		global $conn;
		$to123=$_POST['to_approve'];
		$to = mysqli_real_escape_string($conn,$to123);
		$from123=$_POST['notice_to'];
		$from = mysqli_real_escape_string($conn,$from123);
		$MyDate123=$_POST['date'];
		$MyDate = mysqli_real_escape_string($conn,$MyDate123);
		$content=$_POST["content"];
		$sub='Applications';
		$TypeOfLeave=$_POST['TypeOfLeave'];
		$LeavesNeeded=(int)$_POST['LeavesNeeded'];
		PostToDashBoard();
		
		mysqli_close($conn);
	}	
	else if (isset($_POST['level2_reject'])) {
		global $to,$from,$content,$sub,$MyDate;
		global $conn;
		$to123=$_POST['notice_to'];
		$to = mysqli_real_escape_string($conn,$to123);
		$from123=$_POST['from'];
		$from = mysqli_real_escape_string($conn,$from123);
		$MyDate123=$_POST['date'];
		$MyDate = mysqli_real_escape_string($conn,$MyDate123);
		$TypeOfLeave=$_POST['TypeOfLeave'];
		$content="your application for leave posted on ".$MyDate."has been rejected by ".$from;
		$sub='Responses';
		PostToDashBoard();
		mysqli_close($conn);
	}
	
	else if (isset($_POST['level3_reject'])) {
		global $to,$from,$content,$sub,$MyDate;
		global $conn;
		$to123=$_POST['to'];
		$to = mysqli_real_escape_string($conn,$to123);
		$from123=$_POST['from'];
		$from = mysqli_real_escape_string($conn,$from123);
		$MyDate123=$_POST['date'];
		$MyDate = mysqli_real_escape_string($conn,$MyDate123);
		$content="your application for leave posted on ".$MyDate."has been rejected by ".$from;
		$sub='Responses';
		$TypeOfLeave=$_POST['TypeOfLeave'];
		PostToDashBoard();
		
	}	
} 
?>
