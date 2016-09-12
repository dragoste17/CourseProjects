use strict;
use warnings;
use Player_Multiplayer;

main();

sub main
{
	print "\n\t Tic-Tac-Toe\n";
	print "\nThe board is as follows:\n";
	print "\n 0 | 1 | 2\n";
	print "-----------";
	print "\n 3 | 4 | 5\n";
	print "-----------";
	print "\n 6 | 7 | 8\n";
	print "\nPlayer1: ";
	my $ip = <>;
	while ($ip > 8 or $ip < 0){
		print "Wrong Input. Please try again\n";
		print "\nPlayer1: ";
		$ip = <>;
	}
	$Player_Multiplayer::Array[$ip] = "X";
	print "\n $Player_Multiplayer::Array[0] | $Player_Multiplayer::Array[1] | $Player_Multiplayer::Array[2]\n";
	print "---------";
	print "\n $Player_Multiplayer::Array[3] | $Player_Multiplayer::Array[4] | $Player_Multiplayer::Array[5]\n";
	print "---------";
	print "\n $Player_Multiplayer::Array[6] | $Player_Multiplayer::Array[7] | $Player_Multiplayer::Array[8]\n";

	my $o1 = Player_Multiplayer->new;
	my $o2 = Player_Multiplayer->new;
	my $a = 1;
	while ($Player_Multiplayer::count != 0) {	
		$o2->input2();
		$o2->disp();
		$a = $o2->check();
		if ($a == 10 or $a == 20){
			last;
		}
		$o1->input1();
		$o1->disp();
		$a = $o1->check();
		if ($a == 10 or $a == 20){
			last;
		}
	}
	if ($a == 10 or $a == 20){
		print "Game Over!!\n"
	} else {
		print "\nIt's A Tie!! Well Played.\n"
	}
	return 1;
}
