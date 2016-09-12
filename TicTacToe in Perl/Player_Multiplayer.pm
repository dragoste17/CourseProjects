package Player_Multiplayer;
use strict;
use warnings;

our @Array = ("","","","","","","","","");
our $count = 8;

sub new          # Constructor
{
	my $class = shift;
	my $self = {};
	bless($self, $class);
	return $self;
}

sub input1
{
	my ($self) = @_;
	print "\nPlayer1: ";
	my $ip = <>;
	while ($ip > 8 or $ip < 0 or $Array[$ip] ne ""){
		print "Wrong Input. Please try again\n";
		print "\nPlayer1: ";		
		$ip = <>;
	}
	$Array[$ip] = "X";
	$count -= 1;
}

sub input2
{
	my ($self) = @_;
	print "\nPlayer2: ";
	my $ip = <>;
	while ($ip > 8 or $ip < 0 or $Array[$ip] ne ""){
		print "Wrong Input. Please try again\n";
		print "\nPlayer2: ";		
		$ip = <>;
	}
	$Array[$ip] = "O";
	$count -= 1;
}

sub check
{
	my ($self) = @_;
	if ($Array[0] eq "X" and $Array[1] eq "X" and $Array[2] eq "X" or $Array[3] eq "X" and $Array[4] eq "X" and $Array[5] eq "X" or $Array[6] eq "X" and $Array[7] eq "X" and $Array[8] eq "X" or $Array[0] eq "X" and $Array[3] eq "X" and $Array[6] eq "X" or $Array[1] eq "X" and $Array[4] eq "X" and $Array[7] eq "X" or $Array[2] eq "X" and $Array[5] eq "X" and $Array[8] eq "X" or $Array[0] eq "X" and $Array[4] eq "X" and $Array[8] eq "X" or $Array[2] eq "X" and $Array[4] eq "X" and $Array[6] eq "X"){
		print "\nPlayer1 WINS!! Congratulations!!\n";
		return 10;
	}
	if ($Array[0] eq "O" and $Array[1] eq "O" and $Array[2] eq "O" or $Array[3] eq "O" and $Array[4] eq "O" and $Array[5] eq "O" or $Array[6] eq "O" and $Array[7] eq "O" and $Array[8] eq "O" or $Array[0] eq "O" and $Array[3] eq "O" and $Array[6] eq "O" or $Array[1] eq "O" and $Array[4] eq "O" and $Array[7] eq "O" or $Array[2] eq "O" and $Array[5] eq "O" and $Array[8] eq "O" or $Array[0] eq "O" and $Array[4] eq "O" and $Array[8] eq "O" or $Array[2] eq "O" and $Array[4] eq "O" and $Array[6] eq "O"){
		print "\nPlayer2 WINS!! Congratulations!!\n";
		return 20;
	}
	return 1;
}

sub disp
{
	my ($self) = @_;
	print "\n $Player_Multiplayer::Array[0] | $Player_Multiplayer::Array[1] | $Player_Multiplayer::Array[2]\n";
	print "-----------";
	print "\n $Player_Multiplayer::Array[3] | $Player_Multiplayer::Array[4] | $Player_Multiplayer::Array[5]\n";
	print "-----------";
	print "\n $Player_Multiplayer::Array[6] | $Player_Multiplayer::Array[7] | $Player_Multiplayer::Array[8]\n";
}

1;
