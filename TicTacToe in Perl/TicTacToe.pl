use strict;
use warnings;
use Player;
use Comp;

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
	my $o1 = Player->new;
	my $o2 = Comp->new;
	my $a = 1;
	while ($Player::count != 0) {	
		$o1->input();
		$o1->disp();
		$a = $o1->check();
		if ($a == 10 or $a == 20){
			last;
		}
		if ($Player::count != 0){
			$o2->fill();
			$o2->disp();
			$a = $o2->check();
			if ($a == 10 or $a == 20){
				last;
			}
		}
	}
	if ($a == 10 or $a == 20){
		print "Game Over!!\n"
	} else {
		print "\nIt's A Tie!! Well Played.\n"
	}
	return 1;
}
